import json
import os
from pathlib import Path
from bs4 import BeautifulSoup
import re

# Directories
downloaded_dir = Path("b:/Desktop/leychoon.com/downloaded/www.leychoon.com")
output_dir = Path("b:/Desktop/leychoon.com/content_comparison/original_pages")
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

# Process all HTML files
html_files = list(downloaded_dir.glob("*.html"))
print(f"Found {len(html_files)} HTML files")

original_index = {}

for html_file in html_files:
    try:
        # Read HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract content
        title = extract_title(html_content)
        text = extract_text_from_html(html_content)
        
        # Determine page identifier
        filename = html_file.name
        if filename == "index.html":
            page_id = "home"
        else:
            # Extract page number from filename like "index.html@p=2.html"
            match = re.search(r'@p=(\d+)', filename)
            page_id = f"page_{match.group(1)}" if match else filename.replace('.html', '')
        
        # Create JSON for this page
        page_data = {
            "page_id": page_id,
            "filename": filename,
            "title": title,
            "full_text": text,
            "word_count": len(text.split())
        }
        
        # Save individual JSON
        json_filename = output_dir / f"{page_id}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(page_data, f, ensure_ascii=False, indent=2)
        
        # Add to index
        original_index[page_id] = {
            "title": title,
            "filename": filename,
            "word_count": len(text.split()),
            "json_file": f"original_pages/{page_id}.json"
        }
        
        print(f"Processed: {filename} -> {page_id}.json ({len(text.split())} words)")
    
    except Exception as e:
        print(f"Error processing {html_file.name}: {e}")

# Save original index
index_path = Path("b:/Desktop/leychoon.com/content_comparison/original_index.json")
with open(index_path, 'w', encoding='utf-8') as f:
    json.dump(original_index, f, ensure_ascii=False, indent=2)

print(f"\n✅ Created {len(original_index)} JSON files")
print(f"✅ Original index saved to: {index_path}")
