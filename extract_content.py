"""
Extract text content from all crawled HTML pages into a JSON structure.
This will help identify any missing content in the new site.
"""

import os
import json
import re
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_script = False
        self.in_style = False
        self.title = ""
        self.in_title = False
        self.in_page_title = False
        self.page_title = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.in_script = True
        elif tag == 'style':
            self.in_style = True
        elif tag == 'title':
            self.in_title = True
        # Look for page title div
        attrs_dict = dict(attrs)
        if attrs_dict.get('class') == 'page_title':
            self.in_page_title = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
        elif tag == 'style':
            self.in_style = False
        elif tag == 'title':
            self.in_title = False
        elif tag == 'div' and self.in_page_title:
            self.in_page_title = False

    def handle_data(self, data):
        if self.in_script or self.in_style:
            return
        if self.in_title:
            self.title = data.strip()
        if self.in_page_title:
            self.page_title = data.strip()
        text = data.strip()
        if text and len(text) > 20:  # Only keep meaningful text
            self.text.append(text)

def extract_content(filepath):
    """Extract title and text content from an HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        parser = TextExtractor()
        parser.feed(content)
        
        # Combine text into paragraphs
        full_text = ' '.join(parser.text)
        
        return {
            'title': parser.title or 'Untitled',
            'page_title': parser.page_title or '',
            'text_preview': full_text[:500] + '...' if len(full_text) > 500 else full_text,
            'full_text': full_text
        }
    except Exception as e:
        return {'error': str(e)}

def main():
    base_dir = r'b:\Desktop\leychoon.com\downloaded\www.leychoon.com'
    output = {}
    
    # Find all HTML files
    for filename in os.listdir(base_dir):
        if filename.endswith('.html') and '@p=' in filename:
            filepath = os.path.join(base_dir, filename)
            # Extract page ID from filename
            match = re.search(r'@p=(\d+)', filename)
            page_id = match.group(1) if match else filename
            
            output[page_id] = extract_content(filepath)
            output[page_id]['original_file'] = filename
    
    # Save to JSON
    output_path = r'b:\Desktop\leychoon.com\content_inventory.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"Extracted content from {len(output)} pages")
    print(f"Output saved to: {output_path}")
    
    # Print summary
    print("\n=== Page Inventory ===")
    for page_id, data in sorted(output.items(), key=lambda x: x[0]):
        title = data.get('page_title') or data.get('title', 'Untitled')
        print(f"  {page_id}: {title[:60]}")

if __name__ == '__main__':
    main()
