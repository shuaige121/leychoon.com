import json
from pathlib import Path

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load data
content_inventory = load_json("b:/Desktop/leychoon.com/content_inventory.json")

# Count announcements and press releases
announcements = []
press_releases = []
newsroom = []
financial_results = []

for page_id, data in content_inventory.items():
    title = data.get('page_title', data.get('title', ''))
    
    if 'Announcements' in title:
        announcements.append({
            'id': page_id,
            'title': title,
            'filename': data.get('filename', ''),
            'preview': data.get('text_preview', '')[:200]
        })
    elif 'Press Release' in title:
        press_releases.append({
            'id': page_id,
            'title': title,
            'filename': data.get('filename', ''),
            'preview': data.get('text_preview', '')[:200]
        })
    elif 'Newsroom' in title:
        newsroom.append({
            'id': page_id,
            'title': title,
            'filename': data.get('filename', ''),
            'preview': data.get('text_preview', '')[:200]
        })
    elif 'Financial Results' in title:
        financial_results.append({
            'id': page_id,
            'title': title,
            'filename': data.get('filename', ''),
            'preview': data.get('text_preview', '')[:200]
        })

# Generate report
report = []
report.append("# 历史公告和新闻稿统计报告\n\n")

report.append("## 📢 Announcements (公告)\n\n")
report.append(f"**总页数**: {len(announcements)}\n\n")
report.append("这些是分页的公告列表，原始网站用分页显示。\n\n")
report.append("**建议处理方式**:\n")
report.append("- 在 `investors.html` 的 Newsroom 部分添加一个动态列表\n")
report.append("- 使用 JavaScript 分页或「加载更多」功能\n")
report.append("- 或创建独立的 `announcements.html` 页面\n\n")

report.append("## 📰 Press Releases (新闻稿)\n\n")
report.append(f"**总页数**: {len(press_releases)}\n\n")

report.append("## 📊 Newsroom (新闻室)\n\n")
report.append(f"**总页数**: {len(newsroom)}\n\n")

report.append("## 💰 Financial Results (财务结果)\n\n")
report.append(f"**总页数**: {len(financial_results)}\n\n")

report.append("---\n\n")
report.append("## 总计\n\n")
total = len(announcements) + len(press_releases) + len(newsroom) + len(financial_results)
report.append(f"**历史分页总数**: {total} 个HTML文件\n\n")

report.append("## 💡 实施建议\n\n")
report.append("### 方案1: 整合到现有页面 (推荐)\n")
report.append("在 `investors.html` 添加动态内容区域：\n\n")
report.append("```html\n")
report.append('<section id="announcements-archive">\n')
report.append('  <h2>Historical Announcements</h2>\n')
report.append('  <div id="announcements-list">\n')
report.append('    <!-- 使用JavaScript动态加载 -->\n')
report.append('  </div>\n')
report.append('  <button id="load-more">Load More</button>\n')
report.append('</section>\n')
report.append("```\n\n")

report.append("### 方案2: 创建独立存档页面\n")
report.append("创建以下新页面：\n")
report.append("- `announcements-archive.html` - 所有历史公告\n")
report.append("- `press-releases-archive.html` - 所有新闻稿\n")
report.append("- 从 `investors.html` 链接到这些存档页面\n\n")

report.append("### 数据结构建议\n")
report.append("```javascript\n")
report.append("// announcements-data.js\n")
report.append("const announcements = [\n")
report.append("  {\n")
report.append('    date: "2024-01-20",\n')
report.append('    title: "公告标题",\n')
report.append('    content: "公告内容...",\n')
report.append('    pdfLink: "path/to/file.pdf"\n')
report.append("  },\n")
report.append("  // ...\n")
report.append("];\n")
report.append("```\n\n")

# Save report
report_path = Path("b:/Desktop/leychoon.com/content_comparison/historical_content_report.md")
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(''.join(report))

print(f"✅ 历史内容报告已生成: {report_path}")
print(f"\n📊 统计:")
print(f"  - Announcements: {len(announcements)} 页")
print(f"  - Press Releases: {len(press_releases)} 页")
print(f"  - Newsroom: {len(newsroom)} 页")
print(f"  - Financial Results: {len(financial_results)} 页")
print(f"  - 总计: {total} 页")
