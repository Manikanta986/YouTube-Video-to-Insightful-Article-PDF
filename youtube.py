import os
import zipfile
from dotenv import load_dotenv

from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# ==============================
# 🔑 Load API Key
# ==============================
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env")

# ==============================
# 🤖 Gemini Model
# ==============================
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

# ==============================
# 🧠 Summarizer Prompt
# ==============================
system_message = """You are a Professional Article Writer specializing in Medium, LinkedIn, and tech blogs."""

human_message = """
Transform YouTube transcript into engaging professional articles.

RULES:
- Ignore intro, ads, promotions
- Focus only on technical content
- Use headings, lists, structured format
- Add actionable insights
- End with summary

Transcript:
{transcript}
"""

summarizer_prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("human", human_message)
])

# ==============================
# 📥 Extract Transcript
# ==============================
def extract_transcript(link: str) -> str:
    loader = YoutubeLoader.from_youtube_url(link)
    docs = loader.load()
    return docs[0].page_content

# ==============================
# ✂️ Chunking
# ==============================
def get_text_chunks(text, chunk_size=2000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

# ==============================
# 🧠 Recursive Summarization
# ==============================
def recursive_summarize(text):
    chunks = get_text_chunks(text)
    summaries = []

    for chunk in chunks:
        prompt = summarizer_prompt.invoke({"transcript": chunk})
        response = llm.invoke(prompt)
        summaries.append(response.content)

    return "\n\n".join(summaries)

# ==============================
# 🔹 Base Summarizer
# ==============================
base_summarizer = (
    RunnablePassthrough()
    | RunnableLambda(extract_transcript)
    | summarizer_prompt
    | llm
    | StrOutputParser()
)

# ==============================
# 🔹 Long Summarizer
# ==============================
long_summarizer = (
    RunnablePassthrough()
    | RunnableLambda(extract_transcript)
    | RunnableLambda(recursive_summarize)
)

# ==============================
# 🔍 Length Check
# ==============================
def estimate_transcript_length(link: str) -> bool:
    transcript = extract_transcript(link)
    return len(transcript) >= 1000

# ==============================
# 🌐 Webpage Generator Prompt
# ==============================
web_system = """You are a Senior Frontend Developer.

Output EXACT format:

--html--
HTML code
--html--

--css--
CSS code
--css--

--js--
JavaScript code
--js--
"""

web_human = """
Create a modern article webpage (Medium/Dev.to style).

Requirements:
- Responsive design
- Clean typography
- Dark/light mode
- Smooth UI
- SEO friendly

Content:
{article}
"""

web_prompt = ChatPromptTemplate.from_messages([
    ("system", web_system),
    ("human", web_human)
])

# ==============================
# 🔗 Smart Pipeline
# ==============================
smart_pipeline = RunnableBranch(
    (RunnableLambda(estimate_transcript_length), long_summarizer),
    base_summarizer
) | web_prompt | llm | StrOutputParser()

# ==============================
# ▶️ RUN
# ==============================
url = "https://www.youtube.com/watch?v=9w0QQWXY5go"

result = smart_pipeline.invoke(url)

# ==============================
# 💾 Save Output Files
# ==============================
html = result.split("--html--")[1]
css = result.split("--css--")[1]
js = result.split("--js--")[1]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)

# ==============================
# 📦 ZIP FILE
# ==============================
with zipfile.ZipFile("website.zip", "w") as zipf:
    zipf.write("index.html")
    zipf.write("style.css")
    zipf.write("script.js")

print("✅ Website generated successfully using Gemini!")