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

### 2. 图片下载 (Image Download)
从抓取到的内容中，提取所有图片链接（markdown 格式的 `![alt](url)` 或 HTML 中的 `<img src="...">`）。
在 `inbox/assets/` 目录下创建用于存放图片的子目录，目录名使用 slug。
使用 `curl` 或 `wget` 下载所有图片到该目录，并将 markdown 中的图片路径更新为本地路径（如 `assets/{slug}/图片名.jpg`）。

### 3. 外链提取 (External Links Extraction)
从抓取到的内容中，提取所有外部链接（http/https 开头的，排除图片链接）。
记录这些链接，稍后需要用户判断是否需要追踪。

### 4. 思考与整理 (Digest)
阅读抓取到的内容，进行"脱水"处理：
- **Title**: 提取或生成一个清晰的标题。
- **Category**: 判断它属于哪个领域（例如：`Coding`, `DevOps`, `Product`, `AI`, `Reading`, `Life`）。
- **Summary**: 写一段 100 字以内的中文摘要（TL;DR），总结核心观点。
- **Tags**: 提取 3-5 个相关标签（hashtag 格式，如 #docker #k8s）。
- **Slug**: 生成一个 URL 友好的英文文件名（例如 `docker-best-practices`）。

### 5. 生成文件 (File Generation)
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

{抓取到的原文内容（已更新图片路径）}
```

### 6. Git 同步 (Git Sync)
- 运行 `git add .` 将新生成的文件加入暂存区。
- 运行 `git commit -m "save: {Title}"`。
- 运行 `git push` 将更改同步到远程仓库。

### 7. 外链处理 (External Links Processing)
列出在正文中发现的所有外部链接，格式如下：

**发现的外链：**
1. [链接描述或 URL]
2. ...

请告诉我是否需要进一步追踪这些链接（获取其内容并存入知识库）。
