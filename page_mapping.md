# Ley Choon Website - Page Mapping & Migration Status

This document maps the original crawled pages to the new site structure.

## Legend
- ✅ = Migrated to new site
- ❌ = Not yet migrated
- 🔄 = Partially migrated (content exists but incomplete)

---

## Main Navigation Structure

| # | Page ID | Page Title | Original File | New File | Status |
|---|---------|------------|---------------|----------|--------|
| 1 | - | Home | index.html | index.html | ✅ |
| 2 | 2 | About Us (Landing) | index.html@p=2.html | about.html | ❌ |
| 3 | 28 | Corporate Profile | index.html@p=28.html | about.html#profile | ❌ |
| 4 | 804 | Corporate Video | index.html@p=804.html | about.html#video | ❌ |
| 5 | 34 | Vision and Mission | index.html@p=34.html | about.html#vision | ❌ |
| 6 | 36 | History & Milestones | index.html@p=36.html | about.html#history | ❌ |
| 7 | 32 | Our Group Structure | index.html@p=32.html | about.html#structure | ❌ |
| 8 | 754 | Board of Directors | index.html@p=754.html | about.html#board | ❌ |
| 9 | 289 | Management Team | index.html@p=289.html | about.html#management | ❌ |
| 10 | 38 | Awards & Certifications | index.html@p=38.html | about.html#awards | ❌ |

---

## Our Business Section

| # | Page ID | Page Title | Original File | New File | Status |
|---|---------|------------|---------------|----------|--------|
| 11 | 8 | Our Business (Landing) | index.html@p=8.html | business.html | ❌ |
| 12 | 24 | Pipes and Roads | index.html@p=24.html | business.html#pipes | ❌ |
| 13 | 332 | Asphalt Premix, Milling & Paving | index.html@p=332.html | business.html#asphalt | ❌ |
| 14 | 352 | Project Track Record | index.html@p=352.html | business.html#projects | ❌ |
| 15 | 355 | Our Customers | index.html@p=355.html | business.html#customers | ❌ |
| 16 | 361 | Our Offices & Facilities | index.html@p=361.html | business.html#offices | ❌ |
| 17 | 485 | Our Competitive Strengths | index.html@p=485.html | business.html#strengths | ❌ |
| 18 | 4598 | Portable Traffic Light | index.html@p=4598.html | business.html#traffic-lights | ❌ |

---

## Investor Relations Section

| # | Page ID | Page Title | Original File | New File | Status |
|---|---------|------------|---------------|----------|--------|
| 19 | 2330 | Investor Relations (Landing) | index.html@p=2330.html | investors.html | 🔄 |
| 20 | 903 | Newsroom | index.html@p=903.html | investors.html#newsroom | ❌ |
| 21 | 2679 | Announcements | index.html@p=2679.html | investors.html#announcements | ❌ |
| 22 | 2681 | Press Releases | index.html@p=2681.html | investors.html#press | ❌ |
| 23 | 2439 | Corporate Governance | index.html@p=2439.html | investors.html#governance | ❌ |
| 24 | 2467 | Board of Directors (IR) | index.html@p=2467.html | investors.html#board | ❌ |
| 25 | 2469 | Management Team (IR) | index.html@p=2469.html | investors.html#management | ❌ |
| 26 | 2296 | Financial Information | index.html@p=2296.html | investors.html#financial | ❌ |
| 27 | 2391 | Annual Reports and Circulars | index.html@p=2391.html | investors.html#reports | ❌ |
| 28 | 2334 | Financial Results | index.html@p=2334.html | investors.html#results | ❌ |
| 29 | 3510 | Sustainability Report | index.html@p=3510.html | investors.html#sustainability | ❌ |
| 30 | 2385 | Research Reports | index.html@p=2385.html | investors.html#research | ❌ |
| 31 | 2464 | IR Contact | index.html@p=2464.html | investors.html#contact | ❌ |

---

## Training Programs Section

| # | Page ID | Page Title | Original File | New File | Status |
|---|---------|------------|---------------|----------|--------|
| 32 | 3208 | Training Programs (Landing) | index.html@p=3208.html | training.html | ❌ |
| 33 | 4893 | BCA ATTC | index.html@p=4893.html | training.html#bca-attc | ❌ |
| 34 | 3216 | Course Fees & Registration | index.html@p=3216.html | training.html#fees | ❌ |
| 35 | 3210 | Hydraulic Excavator Operation | index.html@p=3210.html | training.html#excavator | ❌ |
| 36 | 3823 | Bulldozer Operation | index.html@p=3823.html | training.html#bulldozer | ❌ |
| 37 | 3827 | CET Online | index.html@p=3827.html | training.html#cet | ❌ |
| 38 | 4902 | Ley Choon Training Courses | index.html@p=4902.html | training.html#lc-courses | ❌ |
| 39 | 4904 | Essential Road Maintenance | index.html@p=4904.html | training.html#road-maintenance | ❌ |

---

## Other Pages

| # | Page ID | Page Title | Original File | New File | Status |
|---|---------|------------|---------------|----------|--------|
| 40 | 18 | Career | index.html@p=18.html | career.html | ❌ |
| 41 | 20 | Contact Us | index.html@p=20.html | contact.html | 🔄 (in footer) |

---

## Summary

| Section | Total Pages | Migrated | Remaining |
|---------|-------------|----------|-----------|
| Home | 1 | 1 | 0 |
| About Us | 9 | 0 | 9 |
| Our Business | 8 | 0 | 8 |
| Investor Relations | 13 | 1 (partial) | 12 |
| Training Programs | 8 | 0 | 8 |
| Career | 1 | 0 | 1 |
| Contact Us | 1 | 1 (partial) | 0 |
| **TOTAL** | **41** | **3** | **38** |

---

## Migration Approach

For each section, I will create a single-page application with anchor links to subsections:
1. `about.html` - Contains all About Us content with anchor navigation
2. `business.html` - Contains all Business content with anchor navigation  
3. `investors.html` - Contains all Investor Relations content with anchor navigation
4. `training.html` - Contains all Training Programs content with anchor navigation
5. `career.html` - Career page with job listings
6. `contact.html` - Contact information and form

All pages will use the new modern design system (CSS variables, responsive layout) and include multilingual support via the existing `translations.js` mechanism.
