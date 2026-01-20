import json
import re
from pathlib import Path

# Load original Board of Directors data
with open('b:/Desktop/leychoon.com/content_comparison/original_pages/page_754.json', 'r', encoding='utf-8') as f:
    board_data = json.load(f)

text = board_data['full_text']

# Extract director information using patterns
directors = []

# Pattern to find director sections
pattern = r'(Mr|Ms|Dr)\s+([A-Za-z\s,]+?)\s+(Executive|Lead Independent|Independent|Non-Executive)\s+Director[,\s]*(.*?)(?=(?:Mr|Ms|Dr)\s+[A-Za-z\s,]+?\s+(?:Executive|Lead Independent|Independent|Non-Executive)\s+Director|Home\s+\|)'

matches = re.finditer(pattern, text, re.DOTALL)

current_section = ""
for match in matches:
    title = match.group(1)
    name = match.group(2).strip()
    role_type = match.group(3)
    content = match.group(4).strip()
    
    # Clean up role and content
    role_parts = content.split('\n', 1)
    role = role_parts[0].strip() if role_parts else ""
    bio = role_parts[1].strip() if len(role_parts) > 1 else content
    
    # Clean bio
    bio = ' '.join(bio.split())
    
    directors.append({
        'title': title,
        'name': name,
        'role_type': role_type,
        'role': role,
        'bio': bio[:500] if len(bio) > 500 else bio  # Limit to first 500 chars for preview
    })

# Print for verification
print(f"Found {len(directors)} directors\n")
for d in directors:
    print(f"{d['title']} {d['name']}")
    print(f"Role: {d['role']}")
    print(f"Bio length: {len(d['bio'])} chars")
    print("="*50)

# Generate HTML
html_output = []
html_output.append('                <div class="team-card">\n')

for d in directors:
    html_output.append(f'                <div class="team-card">\n')
    html_output.append(f'                    <h3>{d["title"]} {d["name"]}</h3>\n')
    html_output.append(f'                    <p class="position">{d["role"]}</p>\n')
    html_output.append(f'                    <p>{d["bio"]}</p>\n')
    html_output.append(f'                </div>\n')

# Save to file for review
with open('b:/Desktop/leychoon.com/board_members_extracted.txt', 'w', encoding='utf-8') as f:
    for d in directors:
        f.write(f"{d['title']} {d['name']}\n")
        f.write(f"{'='*60}\n")
        f.write(f"Role: {d['role']}\n\n")
        f.write(f"{d['bio']}\n\n")
        f.write(f"{'='*60}\n\n")

print(f"\n✅ Extracted {len(directors)} directors")
print("📄 Details saved to: board_members_extracted.txt")
