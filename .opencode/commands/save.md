---
description: 抓取网页，脱水整理，并存入 Git 仓库
---
我希望将这个链接的内容存入知识库：
"""
$ARGUMENTS
"""

请严格按照以下步骤执行：
1. **抓取**: 运行 `python3 scripts/fetch.py "$ARGUMENTS"` 获取 Markdown 内容。
2. **脱水**: 阅读内容，提取标题(Title)、分类(Category: 如 Tech, Product, Life 等)、3个标签(Tags)、以及一段100字以内的中文摘要(Summary)。
3. **生成文件**: 在 `inbox/` 目录下创建一个 Markdown 文件。文件名为 `YYYY-MM-DD-英文短标题.md`（使用当天的实际日期）。
4. **文件格式**: 
   头部必须包含 YAML Frontmatter (title, date, original_url, category, tags)。
   正文开头引用摘要，随后附上抓取到的完整原文。
5. **持久化**: 执行 `git add .` 和 `git commit -m "Save: {Title}"`。如果遇到 git 配置问题请提醒我。
