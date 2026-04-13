# 🎥 YouTube to Article Website Generator (Gemini + LangChain)

Transform any YouTube video into a **professional article** and automatically generate a **modern responsive website** (HTML, CSS, JS) using Google's Gemini AI.

---

## 🚀 Features

* 🔗 Extracts transcript from YouTube videos
* ✂️ Handles long videos with recursive summarization
* 🧠 Converts transcript into structured **professional articles**
* 🌐 Generates a **Medium/Dev.to style website**
* 🎨 Includes:

  * Responsive design
  * Clean typography
  * Dark/Light mode
  * Smooth UI
* 📦 Automatically exports:

  * `index.html`
  * `style.css`
  * `script.js`
  * `website.zip`

---

## 🛠️ Tech Stack

* Python 🐍
* LangChain
* Google Gemini (`gemini-2.5-flash`)
* YouTube Transcript Loader
* HTML, CSS, JavaScript

---

## 📂 Project Structure

```
├── main.py
├── .env
├── index.html
├── style.css
├── script.js
├── website.zip
└── README.md
```

---

## 🔑 Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/youtube-article-generator.git
cd youtube-article-generator
```

---

### 2. Install Dependencies

```
pip install langchain langchain-community langchain-google-genai python-dotenv
```

---

### 3. Add API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 4. Run the Script

```
python main.py
```

---

## ⚙️ How It Works

### 🔹 Step 1: Extract Transcript

* Uses `YoutubeLoader` to fetch video transcript

### 🔹 Step 2: Smart Summarization

* Short videos → Direct summarization
* Long videos → Chunking + Recursive summarization

### 🔹 Step 3: Article Generation

* Converts transcript into:

  * Structured headings
  * Bullet points
  * Actionable insights

### 🔹 Step 4: Website Creation

* Generates:

  * HTML layout
  * CSS styling
  * JavaScript (dark mode, interactions)

### 🔹 Step 5: Export

* Saves files and compresses into ZIP

---

## 🧠 Pipeline Overview

```
YouTube URL
    ↓
Transcript Extraction
    ↓
Length Check
    ↓
(Small → Direct) OR (Large → Recursive)
    ↓
Article Generation
    ↓
Webpage Generator
    ↓
HTML + CSS + JS
    ↓
ZIP Output
```

---

## 📌 Example

```python
url = "https://www.youtube.com/watch?v=9w0QQWXY5go"
result = smart_pipeline.invoke(url)
```

---

## ⚠️ Notes

* Ensure YouTube video has captions enabled
* API key must be valid
* Large videos may take longer processing time

---

## 📈 Future Improvements

* Add Streamlit UI
* Support multiple videos
* Add blog export (Markdown/PDF)
* SEO optimization enhancements
* Multi-language support

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues for suggestions or improvements.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Bolla Sai Durga Siva Manikanta**

