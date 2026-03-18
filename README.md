# Ley Choon Group — Corporate Website

Modern redesign of [leychoon.com](http://www.leychoon.com) for Ley Choon Group Holdings Limited (SGX: BKV).

A static HTML/CSS/JS site consolidating the original 165-page corporate website into 7 clean, responsive pages.

## Pages

| Page | Description |
|------|-------------|
| `index.html` | Homepage |
| `about.html` | Company profile, vision, board of directors, history |
| `business.html` | Civil engineering, geotechnical, mechanical & electrical |
| `investors.html` | Financial reports, announcements, corporate governance |
| `training.html` | BCA-approved training programs and certifications |
| `career.html` | Job opportunities and company culture |
| `contact.html` | Office locations and contact details |

## Tech Stack

- HTML5, CSS3 (Grid, Flexbox, Custom Properties), vanilla JavaScript
- No framework dependencies
- Python scripts for content extraction and verification (`content_comparison/`)

## Local Development

```bash
git clone https://github.com/shuaige121/leychoon.com.git
cd leychoon.com
npx -y http-server -p 8080 -o
```

Open http://localhost:8080.

## Deployment

Static files — deploy to any hosting provider (Cloudflare Pages, Netlify, S3, etc.) with no build step required.

## Project Structure

```
leychoon.com/
  *.html                  # 7 site pages
  css/styles.css          # Main stylesheet
  js/                     # Core JS and smooth scrolling
  assets/                 # Images and media
  content_comparison/     # Content verification tooling
```

## License

Proprietary. All rights reserved by Ley Choon Group Holdings Limited.
