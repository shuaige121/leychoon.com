document.addEventListener('DOMContentLoaded', () => {
    // Language Switcher Logic
    const langSwitcher = document.getElementById('lang-select');
    const currentLang = localStorage.getItem('site_lang') || 'en';

    // Set initial dropdown value
    if (langSwitcher) {
        langSwitcher.value = currentLang;
        updateLanguage(currentLang);

        langSwitcher.addEventListener('change', (e) => {
            const selectedLang = e.target.value;
            localStorage.setItem('site_lang', selectedLang);
            updateLanguage(selectedLang);
        });
    }

    // Initialize Auto-link logic
    enhanceContactLinks();
});

// PDF Viewer Logic
function openPDF(path) {
    const overlay = document.getElementById('pdf-overlay');
    const frame = document.getElementById('pdf-frame');

    // Set source for Iframe
    frame.src = path;

    // Show overlay
    overlay.classList.add('active');

    // Disable body scroll
    document.body.style.overflow = 'hidden';
}

function closePDF() {
    const overlay = document.getElementById('pdf-overlay');
    const frame = document.getElementById('pdf-frame');

    overlay.classList.remove('active');

    // Reactivate body scroll
    document.body.style.overflow = 'auto';

    // Clear src to stop memory usage
    setTimeout(() => {
        frame.src = '';
    }, 300);
}

function updateLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            // Check if it's an input placeholder or text content
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = translations[lang][key];
            } else {
                element.innerHTML = translations[lang][key];
            }
        }
    });

    // Update HTML lang attribute
    document.documentElement.lang = lang;
}

function enhanceContactLinks() {
    // This function searches for phone numbers and emails in the text ensuring they are properly linked
    // In this specific implementation, we will manually link them in HTML, but this acts as a dynamic safeguard

    // Example: Convert any phone text +65 ... to WhatsApp link if not already a link
    // Implementation omitted for this static rewrite as we control the HTML.
}
