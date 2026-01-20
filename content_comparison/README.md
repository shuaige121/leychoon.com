# 内容对比系统说明

## 文件夹结构

```
content_comparison/
├── original_pages/          # 原始网站的165个页面JSON
│   ├── home.json
│   ├── page_2.json
│   ├── page_8.json
│   └── ... (165个文件)
├── new_pages/               # 新网站的7个页面JSON
│   ├── index.json
│   ├── about.json
│   ├── business.json
│   ├── investors.json
│   ├── training.json
│   ├── career.json
│   └── contact.json
├── original_index.json      # 原始网站全局索引
└── new_index.json          # 新网站全局索引
```

## 文件说明

### 1. original_pages/ (原始网站)
- **数量**: 165个JSON文件
- **来源**: 从 `downloaded/www.leychoon.com/` 提取
- **内容**: 每个HTML页面的所有纯文本内容
- **格式**:
  ```json
  {
    "page_id": "page_2",
    "filename": "index.html@p=2.html",
    "title": "About Us - Ley Choon Group",
    "full_text": "完整的页面文本...",
    "word_count": 1234
  }
  ```

### 2. new_pages/ (新网站)
- **数量**: 7个JSON文件
- **来源**: 从新设计的HTML文件提取
- **内容**: 每个页面的文本内容 + 分节信息
- **格式**:
  ```json
  {
    "page_id": "about",
    "filename": "about.html",
    "title": "About Us - Ley Choon Group",
    "full_text": "完整的页面文本...",
    "word_count": 1600,
    "sections": {
      "profile": "公司简介内容...",
      "vision": "愿景使命内容...",
      ...
    }
  }
  ```

### 3. original_index.json
全局索引，包含所有165个原始页面的元数据：
- 页面标题
- 文件名
- 字数统计
- JSON文件路径

### 4. new_index.json
新网站全局索引，包含7个页面的元数据：
- 页面标题
- 文件名
- 字数统计
- 分节数量
- 各分节名称
- JSON文件路径

## 统计对比

| 指标 | 原始网站 | 新网站 |
|-----|---------|--------|
| 页面数量 | 165 | 7 |
| 总字数 | ~41,000+ | ~5,224 |

### 新网站各页面字数:
- index.html: 215词
- about.html: 1,600词
- business.html: 1,127词
- investors.html: 587词
- training.html: 1,149词
- career.html: 323词
- contact.html: 223词

## 使用方法

### 查看单个页面内容
```python
import json

# 查看原始网站某页
with open('content_comparison/original_pages/page_2.json', 'r', encoding='utf-8') as f:
    page = json.load(f)
    print(page['title'])
    print(page['full_text'])

# 查看新网站某页
with open('content_comparison/new_pages/about.json', 'r', encoding='utf-8') as f:
    page = json.load(f)
    print(page['title'])
    print(page['sections']['profile'])  # 查看特定分节
```

### 使用索引快速查找
```python
import json

# 加载索引
with open('content_comparison/original_index.json', 'r', encoding='utf-8') as f:
    original_index = json.load(f)

# 查找特定标题的页面
for page_id, info in original_index.items():
    if 'Board of Directors' in info['title']:
        print(f"找到: {info['title']} - {info['json_file']}")
```

## 对比建议

1. **结构对比**: 对比 original_index.json 和 new_index.json
2. **内容对比**: 使用文本对比工具比较具体JSON文件
3. **字数检查**: 确认重要内容的字数是否相近
4. **分节检查**: 确认新网站各分节是否包含相应的原始内容

## 下一步

可以使用这些JSON文件进行:
1. 自动化内容对比
2. 关键词搜索
3. 内容完整性验证
4. 缺失内容识别
