---
description: 抓取网页，脱水整理，并存入 Git 仓库
---
我希望将这个链接的内容存入知识库：
"""
$ARGUMENTS
"""

请严格按照以下步骤执行（Do not skip steps）：

### 1. 抓取 (Fetch)
运行 `python3 scripts/fetch.py "$ARGUMENTS"` 获取网页的 Markdown 内容。
如果抓取失败，请停止并报错。

### 2. 思考与整理 (Digest)
阅读抓取到的内容，进行"脱水"处理：
- **Title**: 提取或生成一个清晰的标题。
- **Category**: 判断它属于哪个领域（例如：`Coding`, `DevOps`, `Product`, `AI`, `Reading`, `Life`）。
- **Summary**: 写一段 100 字以内的中文摘要（TL;DR），总结核心观点。
- **Tags**: 提取 3-5 个相关标签（hashtag 格式，如 #docker #k8s）。
- **Slug**: 生成一个 URL 友好的英文文件名（例如 `docker-best-practices`）。

### 3. 生成文件 (File Generation)
在 `inbox/` 目录下创建一个新的 Markdown 文件。
文件名格式：`YYYY-MM-DD-{slug}.md` (使用今日日期)。

**文件内容模板（请严格遵守）：**
```markdown
---
title: "{Title}"
date: {YYYY-MM-DD}
original_url: "$ARGUMENTS"
category: {Category}
tags: [{Tags}]
---

# {Title}

> **摘要**：{Summary}

---

## 正文内容

{抓取到的原文内容}
```
