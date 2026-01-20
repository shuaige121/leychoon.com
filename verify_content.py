import json
from pathlib import Path
from difflib import SequenceMatcher

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def similarity_ratio(text1, text2):
    """Calculate similarity between two texts"""
    return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

def find_text_in_original(search_text, original_text):
    """Check if search text exists in original"""
    search_lower = search_text.lower().strip()
    original_lower = original_text.lower()
    
    # Direct search
    if search_lower in original_lower:
        return True, 1.0
    
    # Fuzzy search for partial matches
    words = search_lower.split()
    if len(words) > 5:
        # Check if most words are present
        found_words = sum(1 for word in words if len(word) > 3 and word in original_lower)
        ratio = found_words / len(words)
        return ratio > 0.7, ratio
    
    return False, 0.0

# Load indices
base_dir = Path("b:/Desktop/leychoon.com/content_comparison")
original_index = load_json(base_dir / "original_index.json")
new_index = load_json(base_dir / "new_index.json")
content_inventory = load_json("b:/Desktop/leychoon.com/content_inventory.json")

# Page mapping: new page -> original page IDs
page_mapping = {
    "about": {
        "name": "About Us",
        "original_pages": ["2", "28", "34", "36", "32", "38", "754", "2467", "289", "2469"],
        "sections": {
            "profile": ["2", "28"],
            "vision": ["34"],
            "history": ["36"],
            "structure": ["32"],
            "board": ["754", "2467"],
            "management": ["289", "2469"],
            "awards": ["38"]
        }
    },
    "business": {
        "name": "Our Business",
        "original_pages": ["8", "24", "332", "352", "355", "361", "485", "4598"],
        "sections": {
            "overview": ["8"],
            "pipes": ["24"],
            "asphalt": ["332"],
            "projects": ["352"],
            "customers": ["355"],
            "offices": ["361"],
            "strengths": ["485"],
            "traffic-lights": ["4598"]
        }
    },
    "investors": {
        "name": "Investor Relations",
        "original_pages": ["2330", "2334", "2385", "2391", "2296", "2439", "2464", "2679", "2681", "3510"],
        "sections": {
            "overview": ["2330"],
            "financial": ["2334", "2391", "2296"],
            "research": ["2385"],
            "governance": ["2439"],
            "contact": ["2464"],
            "newsroom": ["2679", "2681"],
            "sustainability": ["3510"]
        }
    },
    "training": {
        "name": "Training Programs",
        "original_pages": ["3208", "4893", "3210", "3823", "3827", "3216", "4902", "4904"],
        "sections": {
            "overview": ["3208"],
            "bca-attc": ["4893"],
            "excavator": ["3210"],
            "bulldozer": ["3823"],
            "cet": ["3827"],
            "fees": ["3216"],
            "lc-courses": ["4902"],
            "road-maintenance": ["4904"]
        }
    },
    "career": {
        "name": "Career",
        "original_pages": ["18"],
        "sections": {}
    },
    "contact": {
        "name": "Contact Us",
        "original_pages": ["20"],
        "sections": {}
    }
}

# Generate comparison report
report = []
report.append("# 逐页内容核对报告\n\n")

for page_id, page_info in page_mapping.items():
    report.append(f"## {page_info['name']} ({page_id}.html)\n\n")
    
    # Load new page
    new_page_path = base_dir / "new_pages" / f"{page_id}.json"
    if not new_page_path.exists():
        report.append(f"⚠️ 新页面JSON不存在\n\n")
        continue
    
    new_page = load_json(new_page_path)
    
    report.append(f"**新页面字数**: {new_page['word_count']}\n")
    report.append(f"**分节数量**: {len(new_page.get('sections', {}))}\n\n")
    
    # Calculate original total words
    original_total_words = 0
    original_pages_found = []
    
    for orig_id in page_info['original_pages']:
        # Find in content_inventory
        found = False
        for inv_id, inv_data in content_inventory.items():
            if inv_id == orig_id or inv_id == f"page_{orig_id}":
                original_total_words += len(inv_data['full_text'].split())
                original_pages_found.append({
                    'id': orig_id,
                    'title': inv_data.get('page_title', inv_data.get('title', 'Unknown')),
                    'words': len(inv_data['full_text'].split()),
                    'text': inv_data['full_text']
                })
                found = True
                break
        
        if not found:
            report.append(f"⚠️ 未找到原始页面: {orig_id}\n")
    
    report.append(f"**原始页面总字数**: {original_total_words} (来自{len(original_pages_found)}个页面)\n\n")
    
    # Word count comparison
    ratio = new_page['word_count'] / original_total_words if original_total_words > 0 else 0
    if ratio > 0.8:
        status = "✅ 字数充足"
    elif ratio > 0.5:
        status = "⚠️ 字数偏少"
    else:
        status = "❌ 字数严重不足"
    
    report.append(f"**字数比例**: {ratio:.1%} - {status}\n\n")
    
    # Section-by-section comparison
    if page_info['sections']:
        report.append("### 分节详细对比\n\n")
        
        for section_id, orig_ids in page_info['sections'].items():
            section_text = new_page.get('sections', {}).get(section_id, '')
            section_words = len(section_text.split()) if section_text else 0
            
            # Get original section text
            orig_section_text = []
            orig_section_words = 0
            for orig_id in orig_ids:
                for orig_page in original_pages_found:
                    if orig_page['id'] == orig_id:
                        orig_section_text.append(orig_page['text'])
                        orig_section_words += orig_page['words']
            
            combined_orig = ' '.join(orig_section_text)
            
            # Check if content exists
            if section_text and combined_orig:
                found, similarity = find_text_in_original(section_text[:500], combined_orig)
                match_status = "✅" if found else "❌"
            else:
                match_status = "⚠️"
                similarity = 0
            
            report.append(f"- **{section_id}**: {section_words}词 (原始: {orig_section_words}词) - {match_status}\n")
    
    report.append("\n---\n\n")

# Save report
report_path = base_dir / "verification_report.md"
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(''.join(report))

print(f"✅ 核对报告已生成: {report_path}")
print(f"\n📊 总共检查了 {len(page_mapping)} 个新页面")
