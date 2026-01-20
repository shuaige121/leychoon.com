# Ley Choon Group Website

> 🏗️ Modern corporate website redesign for Ley Choon Group Holdings Limited - A leading infrastructure and construction company listed on SGX.

![Project Status](https://img.shields.io/badge/status-in_development-yellow)
![License](https://img.shields.io/badge/license-proprietary-red)

## 📋 Project Overview

This is a complete redesign of the Ley Choon Group corporate website, featuring a modern, premium aesthetic while maintaining comprehensive content from the original site. The project emphasizes user experience, visual excellence, and content integrity.

**Original Site:** [www.leychoon.com](http://www.leychoon.com)  
**Company:** Ley Choon Group Holdings Limited (SGX: BKV)

## ✨ Key Features

### 🎨 Modern Premium Design
- **Glassmorphism UI** with frosted glass effects and subtle animations
- **Dark gradient themes** with vibrant accent colors
- **Smooth micro-interactions** for enhanced user engagement
- **Responsive layouts** optimized for all devices

### 📱 Enhanced Mobile Experience
- **WhatsApp Integration** - Direct messaging via phone number links
- **One-tap Email** - `mailto:` links for instant communication
- **Touch-optimized** navigation and interactions

### 🌐 Multilingual Support (Planned)
- English (Primary)
- Chinese (中文)
- Malay (Bahasa Melayu)
- Tamil (தமிழ்)

### 📊 Comprehensive Content
- **About Us** - Company profile, vision, mission, board of directors, history
- **Business Segments** - Civil engineering, geotechnical, mechanical & electrical
- **Investors** - Financial reports, announcements, corporate governance
- **Training Academy** - BCA-approved training programs
- **Careers** - Job opportunities and company culture
- **Contact** - Multiple contact methods and office locations

## 🗂️ Project Structure

```
leychoon.com/
├── index.html              # Homepage
├── about.html              # Company information
├── business.html           # Business segments
├── investors.html          # Investor relations
├── training.html           # Training academy
├── career.html             # Career opportunities
├── contact.html            # Contact information
├── css/
│   └── styles.css         # Main stylesheet
├── js/
│   ├── main.js            # Core functionality
│   └── smooth-scroll.js   # Smooth scrolling
├── assets/                 # Images and media files
├── content_comparison/     # Content verification system
│   ├── original_pages/    # Original site content (165 pages)
│   ├── new_pages/         # New site content (7 pages)
│   ├── original_index.json
│   ├── new_index.json
│   ├── verification_report.md
│   ├── content_checklist.md
│   └── historical_content_report.md
└── downloaded/             # Original site backup
```

## 🛠️ Technology Stack

- **HTML5** - Semantic markup
- **CSS3** - Custom styles with modern features (Grid, Flexbox, Custom Properties)
- **Vanilla JavaScript** - No framework dependencies
- **Python** - Content extraction and verification scripts

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Node.js (for local development server)
- Python 3.x (for content verification scripts)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/leychoon.com.git
   cd leychoon.com
   ```

2. **Start local development server**
   ```bash
   npx -y http-server -p 8080 -o
   ```

3. **View in browser**
   - Open http://localhost:8080

## 📝 Content Verification System

The project includes a comprehensive content comparison framework to ensure all content from the original site is preserved.

### Scripts

- **`extract_original_content.py`** - Extracts content from original 165 HTML files
- **`extract_new_content.py`** - Extracts content from new 7 HTML pages
- **`verify_content.py`** - Compares and generates verification report
- **`create_checklist.py`** - Creates detailed content restoration checklist
- **`analyze_historical.py`** - Analyzes historical announcements and press releases

### Running Verification

```bash
# Extract original content
python extract_original_content.py

# Extract new content
python extract_new_content.py

# Verify and compare
python verify_content.py

# Generate checklist
python create_checklist.py

# Analyze historical content
python analyze_historical.py
```

### Reports

- **`verification_report.md`** - Page-by-page content comparison
- **`content_checklist.md`** - Detailed missing content breakdown
- **`historical_content_report.md`** - Historical data analysis

## 📊 Content Statistics

| Metric | Original Site | New Site |
|--------|--------------|----------|
| Total Pages | 165 | 7 |
| Word Count | ~41,000+ | ~5,224 |
| Sections | Multiple | Consolidated |

**Note:** The page count difference is due to consolidation of duplicate content and pagination pages.

### New Site Page Breakdown

| Page | Word Count | Sections |
|------|-----------|----------|
| index.html | 215 | Hero, Stats, Features, CTA |
| about.html | 1,600 | Profile, Vision, Board, History |
| business.html | 1,127 | Civil, Geotechnical, M&E |
| investors.html | 587 | Reports, Announcements, Governance |
| training.html | 1,149 | Programs, Certifications, Courses |
| career.html | 323 | Culture, Opportunities, Benefits |
| contact.html | 223 | Offices, Map, Form |

## 🎯 Design Philosophy

### Visual Excellence
- **Premium aesthetics** that wow users at first glance
- **Curated color palettes** using HSL for harmony
- **Modern typography** (Inter, custom web fonts)
- **Smooth gradients** and glass effects
- **Micro-animations** for engagement

### User Experience
- **Intuitive navigation** with smooth scrolling
- **Fast loading times** with optimized assets
- **Accessible design** following WCAG guidelines
- **Mobile-first** approach

### Technical Excellence
- **Semantic HTML** for SEO and accessibility
- **Clean CSS architecture** with CSS custom properties
- **Progressive enhancement**
- **Performance optimization**

## 🔄 Development Status

### ✅ Completed
- [x] Initial design and layout
- [x] All 7 main pages created
- [x] Responsive navigation
- [x] Content extraction framework
- [x] Board of Directors section (about.html)
- [x] Content verification system
- [x] Historical content analysis

### 🚧 In Progress
- [ ] Content restoration from original site
- [ ] Historical announcements integration
- [ ] CSS refactoring (inline to external)
- [ ] Multilingual support implementation

### 📅 Planned
- [ ] Dynamic content loading
- [ ] Search functionality
- [ ] News/announcements archive
- [ ] Investor portal enhancements
- [ ] Contact form backend integration

## 📄 License

This project is proprietary and confidential. All rights reserved by Ley Choon Group Holdings Limited.

## 🤝 Contributing

This is a private corporate project. For internal development inquiries, please contact the project team.

## 📞 Contact

**Ley Choon Group Holdings Limited**
- 📍 3 Sungei Kadut Street 4, Singapore 729053
- 📞 +65 6269 8222
- 📧 enquiries@leychoon.com
- 🌐 www.leychoon.com

---

*Last Updated: January 2026*
