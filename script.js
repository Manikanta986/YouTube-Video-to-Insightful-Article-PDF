
document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Function to set the theme class on the body and update localStorage
    const setTheme = (theme) => {
        if (theme === 'dark') {
            body.classList.add('dark-mode');
        } else {
            body.classList.remove('dark-mode');
        }
        localStorage.setItem('theme', theme);
    };

    // Check for saved theme preference in localStorage
    const savedTheme = localStorage.getItem('theme');
    // Check for user's system preference
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    // Apply theme based on preference: localStorage > system preference > default light
    if (savedTheme) {
        setTheme(savedTheme);
    } else if (prefersDark) {
        setTheme('dark');
    } else {
        setTheme('light'); // Default to light if no preference is found
    }

    // Add event listener to the theme toggle button
    themeToggle.addEventListener('click', () => {
        // Toggle between 'dark' and 'light' themes
        if (body.classList.contains('dark-mode')) {
            setTheme('light');
        } else {
            setTheme('dark');
        }
    });
});
