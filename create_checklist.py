import json
from pathlib import Path

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load data
content_inventory = load_json("b:/Desktop/leychoon.com/content_inventory.json")
base_dir = Path("b:/Desktop/leychoon.com/content_comparison")

# Detailed checklist
checklist = []
checklist.append("# 详细内容补充清单\n\n")

# About page detailed check
checklist.append("## 1. About Us 页面 - 需要补充的内容\n\n")

checklist.append("### 📋 Corporate Profile (profile section)\n")
checklist.append("**原始页面**: page_2, page_28\n")
checklist.append("**当前字数**: 475词 | **原始字数**: 1196词 | **缺失**: 60%\n\n")
checklist.append("**需要检查的内容**:\n")
orig_profile = content_inventory.get('2', {}).get('full_text', '')[:500]
checklist.append(f"- 公司简介是否包含完整的业务描述\n")
checklist.append(f"- 公司历史背景信息\n")
checklist.append(f"- 核心业务领域说明\n\n")

checklist.append("### 📋 Board of Directors (board section)\n")
checklist.append("**原始页面**: page_754, page_2467\n")
checklist.append("**当前字数**: 311词 | **原始字数**: 2847词 | **缺失**: 89%\n\n")
checklist.append("**⚠️ 严重不足！需要检查**:\n")
for inv_id in ['754', '2467']:
    page_data = content_inventory.get(inv_id, {})
    if page_data:
        checklist.append(f"- **{page_data.get('page_title', 'Unknown')}**: {len(page_data.get('full_text', '').split())}词\n")
checklist.append("\n**需要包含的董事信息**:\n")
checklist.append("- 每位董事的完整简介\n")
checklist.append("- 教育背景\n")
checklist.append("- 专业经验\n")
checklist.append("- 在公司的职责\n\n")

checklist.append("### 📋 Management Team (management section)\n")
checklist.append("**原始页面**: page_289, page_2469\n")
checklist.append("**当前字数**: 245词 | **原始字数**: 1683词 | **缺失**: 85%\n\n")
checklist.append("**⚠️ 严重不足！需要包含**:\n")
checklist.append("- 所有管理层成员的完整简介\n")
checklist.append("- 详细的职业背景\n")
checklist.append("- 专业资质\n\n")

checklist.append("### 📋 History & Milestones (history section)\n")
checklist.append("**原始页面**: page_36\n")
checklist.append("**当前字数**: 251词 | **原始字数**: 628词 | **缺失**: 60%\n\n")
checklist.append("**需要检查的时间线**:\n")
page_36 = content_inventory.get('36', {})
if page_36:
    text = page_36.get('full_text', '')
    # Try to extract years
    import re
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    if years:
        checklist.append(f"- 原始页面包含以下年份: {', '.join(sorted(set(years)))}\n")
checklist.append("- 检查所有关键里程碑是否已包含\n\n")

checklist.append("### 📋 Awards & Certifications (awards section)\n")
checklist.append("**原始页面**: page_38\n")
checklist.append("**当前字数**: 132词 | **原始字数**: 747词 | **缺失**: 82%\n\n")
checklist.append("**⚠️ 严重不足！需要包含**:\n")
checklist.append("- 所有奖项的完整列表\n")
checklist.append("- 所有认证证书\n")
checklist.append("- ISO认证详情\n")
checklist.append("- BizSafe认证\n")
checklist.append("- 其他行业认证\n\n")

checklist.append("---\n\n")

# Business page
checklist.append("## 2. Business 页面 - 需要补充的内容\n\n")

checklist.append("### 📋 Project Track Record (projects section)\n")
checklist.append("**原始页面**: page_352\n")
checklist.append("**当前字数**: 301词 | **原始字数**: 1034词 | **缺失**: 71%\n\n")
checklist.append("**⚠️ 严重不足！需要包含**:\n")
page_352 = content_inventory.get('352', {})
if page_352:
    text = page_352.get('full_text', '')
    # Count project mentions
    project_count = text.count('Project') + text.count('project')
    checklist.append(f"- 原始页面提到约 {project_count} 个项目\n")
checklist.append("- 所有重要项目的完整列表\n")
checklist.append("- 项目描述\n")
checklist.append("- 项目规模和价值\n\n")

checklist.append("### 📋 Competitive Strengths (strengths section)\n")
checklist.append("**原始页面**: page_485\n")
checklist.append("**当前字数**: 155词 | **原始字数**: 467词 | **缺失**: 67%\n\n")
checklist.append("**需要包含所有竞争优势点**\n\n")

checklist.append("---\n\n")

# Training page
checklist.append("## 3. Training Programs 页面 - 需要补充的内容\n\n")

for section_id, orig_id in [
    ("excavator", "3210"),
    ("bulldozer", "3823"),
    ("cet", "3827"),
    ("fees", "3216")
]:
    page_data = content_inventory.get(orig_id, {})
    if page_data:
        orig_words = len(page_data.get('full_text', '').split())
        checklist.append(f"### 📋 {page_data.get('page_title', section_id)}\n")
        checklist.append(f"**原始字数**: {orig_words}词\n\n")
        checklist.append("**需要包含的课程信息**:\n")
        checklist.append("- 完整的课程描述\n")
        checklist.append("- 学习成果 (Learning Outcomes)\n")
        checklist.append("- 课程时长\n")
        checklist.append("- 费用详情\n")
        checklist.append("- 报名要求\n\n")

# Summary
checklist.append("---\n\n")
checklist.append("## 📊 总结建议\n\n")
checklist.append("### 🔴 高优先级（缺失>70%）\n")
checklist.append("1. **About Us - Board of Directors** (缺失89%)\n")
checklist.append("2. **About Us - Management Team** (缺失85%)\n")
checklist.append("3. **About Us - Awards & Certifications** (缺失82%)\n")
checklist.append("4. **Business - Project Track Record** (缺失71%)\n\n")

checklist.append("### 🟡 中优先级（缺失50-70%）\n")
checklist.append("1. **About Us - Corporate Profile** (缺失60%)\n")
checklist.append("2. **About Us - History & Milestones** (缺失60%)\n")
checklist.append("3. **Business - Competitive Strengths** (缺失67%)\n")
checklist.append("4. 多个 Training 课程详情\n\n")

checklist.append("### ✅ 已完成（字数充足）\n")
checklist.append("1. **Career page** (174.6%)\n")
checklist.append("2. **Contact Us page** (137.7%)\n\n")

# Save checklist
checklist_path = base_dir / "content_checklist.md"
with open(checklist_path, 'w', encoding='utf-8') as f:
    f.write(''.join(checklist))

print(f"✅ 详细清单已生成: {checklist_path}")
