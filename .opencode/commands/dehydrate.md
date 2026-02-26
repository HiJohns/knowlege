---
description: 接收 Raw HTML/Text，清洗噪音，提取核心事实并存档
---
我有一段未经处理的原始文本（可能是 HTML 片段、乱码或富文本），请帮我"脱水"并存入知识库：

"""
$ARGUMENTS
"""

请严格按照以下步骤执行：

### 1. 清洗与降噪 (Clean & Purify)
- 忽略所有 HTML 标签（如 `<p>`, `<span>`, `div`）、属性（`data-pid`, `class`）和乱码。
- 仅保留核心文本内容。
- **关键数据保留**：文中出现的任何 **数字、统计数据、年份、金额** 必须完整保留，不得模糊化。

### 2. 深度脱水 (Deep Distill)
阅读清洗后的文本，重组为结构化笔记：
- **Title**: 从内容中分析出最核心的标题（如果是 HTML，优先找 h1-h6 内容；如果没有，自己总结）。
- **Summary**: 一句话总结这段文本的核心价值。
- **Key Points**: 将长文逻辑拆解为 Bullet Points。
- **Evidence**: 提取文中支持观点的关键数据/案例（非常重要，这是"干货"所在）。

### 3. 生成文件 (File Generation)
在 `inbox/` 目录下创建一个新的 Markdown 文件。
文件名格式：`YYYY-MM-DD-clip-{slug}.md`。

**文件内容模板：**
```markdown
---
title: "{Title}"
date: {YYYY-MM-DD}
type: clipping
tags: [raw-data, {自动生成的标签}]
---

# {Title}

> **一句话总结**：{Summary}

## 核心观点 (Key Takeaways)
- {观点1}
- {观点2}
...

## 关键数据与证据 (Fact Sheet)
- {比如：新疆粮食单产 552.8公斤，全国第一}
- {比如：亩均毛收入超过 3500 元}
...

---

## 原始文本清洗版 (Original Content)

{这里放入清洗掉 HTML 标签后的纯文本，保留段落结构}
```
