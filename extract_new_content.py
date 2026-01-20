import json
import os
from pathlib import Path
from bs4 import BeautifulSoup
import re

# Directories
new_site_dir = Path("b:/Desktop/leychoon.com")
output_dir = Path("b:/Desktop/leychoon.com/content_comparison/new_pages")
output_dir.mkdir(parents=True, exist_ok=True)

def extract_text_from_html(html_content):
    """Extract clean text from HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Get text
    text = soup.get_text()
    
    # Clean up whitespace
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = ' '.join(chunk for chunk in chunks if chunk)
    
    return text

def extract_title(html_content):
    """Extract page title"""
    soup = BeautifulSoup(html_content, 'html.parser')
    title_tag = soup.find('title')
    return title_tag.get_text().strip() if title_tag else "Untitled"

def extract_sections(html_content):
    """Extract content by sections"""
    soup = BeautifulSoup(html_content, 'html.parser')
    sections = {}
    
    # Find all sections with id
    for section in soup.find_all(['section', 'div'], id=True):
        section_id = section.get('id')
        # Remove scripts and styles from section
        for script in section(["script", "style"]):
            script.decompose()
        section_text = section.get_text()
        # Clean text
        lines = (line.strip() for line in section_text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = ' '.join(chunk for chunk in chunks if chunk)
        sections[section_id] = clean_text
    
    return sections

# New website pages
new_pages = {
    "index": "index.html",
    "about": "about.html", 
    "business": "business.html",
    "investors": "investors.html",
    "training": "training.html",
    "career": "career.html",
    "contact": "contact.html"
}

new_index = {}

for page_id, filename in new_pages.items():
    html_path = new_site_dir / filename
    
    if not html_path.exists():
        print(f"⚠️  File not found: {filename}")
        continue
    
    try:
        # Read HTML
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract content
        title = extract_title(html_content)
        full_text = extract_text_from_html(html_content)
        sections = extract_sections(html_content)
        
        # Calculate word count properly
        words = full_text.split()
        word_count = len(words)
        
        page_data = {
            "page_id": page_id,
            "filename": filename,
            "title": title,
            "full_text": full_text,
            "word_count": word_count,
            "sections": sections
        }
        
        # Save individual JSON
        json_filename = output_dir / f"{page_id}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(page_data, f, ensure_ascii=False, indent=2)
        
        # Add to index
        new_index[page_id] = {
            "title": title,
            "filename": filename,
            "word_count": word_count,
            "section_count": len(sections),
            "sections": list(sections.keys()),
            "json_file": f"new_pages/{page_id}.json"
        }
        
        print(f"Processed: {filename} -> {page_id}.json ({word_count} words, {len(sections)} sections)")
    
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Save new index
index_path = Path("b:/Desktop/leychoon.com/content_comparison/new_index.json")
with open(index_path, 'w', encoding='utf-8') as f:
    json.dump(new_index, f, ensure_ascii=False, indent=2)

print(f"\n✅ Created {len(new_index)} JSON files")
print(f"✅ New site index saved to: {index_path}")

# Create comparison summary
print("\n📊 Comparison Summary:")
original_pages = list(Path('b:/Desktop/leychoon.com/content_comparison/original_pages').glob('*.json'))
print(f"Original site: {len(original_pages)} pages")
print(f"New site: {len(new_index)} pages")
