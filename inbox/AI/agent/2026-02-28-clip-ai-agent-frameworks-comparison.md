---
title: "AI Agent开发框架全面对比：主流框架横评与选型指南"
date: 2026-02-28
type: clipping
tags: [raw-data, AI, Agent, 框架对比, LangChain, Claude, Vercel]
---

# AI Agent开发框架全面对比：主流框架横评与选型指南

> **一句话总结**：本文详细对比了主流AI Agent开发框架（LangChain/LangGraph、Claude Agent SDK、Vercel AI SDK、pi-mono、Pydantic AI、Google ADK、AWS Strands Agents）的功能特性、适用场景和选型建议，为开发者提供技术选型参考。

## 核心观点 (Key Takeaways)

### 框架生态概览
- 主流框架多为大厂出品：Anthropic Claude Agent SDK、Vercel AI SDK、Google ADK、AWS Strands Agents
- 也有个人/社区框架：pi-mono(Pi)、Pydantic AI
- LangChain/LangGraph是AI应用开发老牌框架，生态最完整但学习曲线偏高

### 各框架特点
- **Claude Agent SDK**: 源自Claude Code，抽象程度高，上手快，适合开发类似Claude Code的复杂Agent或企业级应用
- **Vercel AI SDK**: 多模型支持最好，与Next.js/React/Vue等前端框架适配佳，适合Web端AI应用，新手最佳选择
- **pi-mono(Pi)**: 极简主义，内置功能少但学习成本最低，适合快速开发个人项目
- **Pydantic AI**: Python生态，数据验证能力强，适合Python开发者
- **Google ADK**: 模型无关，支持Python/TypeScript/Go/Java四语言，深度整合Google生态(Gemini、GCP、Workspace)
- **AWS Strands Agents**: 模型驱动，API简洁，与AWS生态深度绑定(Bedrock、Lambda)
- **LangChain/LangGraph**: 功能完备，生态完整，支持多智能体协作、循环/分支/重试，但学习成本高

### 选型建议
- 个人项目快速上手：pi-mono、Vercel AI SDK
- Web端AI Agent：Vercel AI SDK
- 复杂/企业级Agent：Claude Agent SDK、LangChain/LangGraph
- Python开发者：Pydantic AI
- 出海/海外企业+Google生态：Google ADK
- 出海/海外企业+AWS生态：AWS Strands Agents

## 关键数据与证据 (Fact Sheet)

### 下载量对比（每周）
- LangChain/LangGraph: 百万级
- Vercel AI SDK、Claude Agent SDK、Pydantic AI: 百万级
- AWS Strands Agents: 相对小众
- pi-mono: 最近因OpenClaw大火，Star数激增

### 语言支持
- Google ADK: 唯一支持Python/TypeScript/Go/Java四种语言
- Vercel AI SDK: TypeScript为主，Python版用的人不多
- Pydantic AI: 仅Python
- pi-mono: 仅TypeScript

### 生态集成
- Vercel AI SDK: Next.js、Edge Functions、KV存储
- Google ADK: Gemini模型、GCP、Google Workspace
- AWS Strands Agents: Bedrock、Lambda、Step Functions、IAM

---

## 原始文本清洗版 (Original Content)

现在 AI Agent 的开发框架确实不少，Anthropic 的 Claude Agent SDK，Vercel 的 AI SDK，Google 的 ADK，AWS 的 Strands Agents，Pydantic 的 Pydantic AI，OpenClaw 背后的 pi-mono(Pi)，当然还有 LangChain 和 LangGraph。

我让 Claude Code 帮我搜集资料，做了一个 AI Agent 框架对比的网页，然后人工验证和修正了其中的一些数据。

在这里，结合网页的内容，简单介绍下当下主流的 AI Agent 开发框架。

### 概览

目前比较常用和主流的 AI Agent 开发框架，大概是下面这几个。绝大多数都是大厂出品，也有个人开发的框架。

![框架概览](assets/ai-agent-frameworks-comparison/v2-efb409268c4d7402d929f67d3e8f4daa_1440w.jpg)

以下是关于这些框架的横向对比：

![横向对比](assets/ai-agent-frameworks-comparison/v2-e5205c20aba94cdb3b77c519c333dd9e_1440w.jpg)

像 Claude Agent SDK、Vercel AI SDK、Google ADK 等公司出品的框架，功能都比较丰富，封装度也比较高。

而 OpenClaw 依赖的 pi-mono(Pi) 则主打极简主义，内置功能不多，但学习成本低，开发快。

另外 LangChain 和 LangGraph（基于 LangChain）算是 AI 应用开发的前辈框架了，功能完备，生态完整，但学习曲线偏高。

这里也简单让 Claude Code 做了一个能力矩阵的对比图：

![能力矩阵](assets/ai-agent-frameworks-comparison/v2-9d7b1b4720dbdda827e8c86884e275ac_1440w.jpg)

上面的排序是一个大致结果，并不绝对。比如学习门槛这块，pi-mono、Vercel AI SDK、Strands Agents 等其实都相对比较简单，而 LangChain 和 LangGraph 的门槛要高出不少。

使用数据方面，我整理了下这些框架在 Github 上的 Star 数。由于 LangChain 是老牌框架，最早用来开发 LLM 应用，所以 Star 数比较多。排除 LangChain，可以看到 LangGraph、Vercel AI SDK 等框架的人气比较高，pi-mono 最近人气也涨上来了。

![Star数对比](assets/ai-agent-frameworks-comparison/v2-0ad7a40b769a18e04a4c99dcafe0d37b_1440w.jpg)

下载量则更能反应实际使用情况。因为有的框架是 TypeScript 的，有的是 Python 的，有的两者都有。我让 Claude Code 综合 npm.js 和 PyPI 上的数据，简单统计了下。可以看到，除了 AWS 的 Strands Agents，其他框架都有每周百万级别的下载。

![下载量对比](assets/ai-agent-frameworks-comparison/v2-b1a424a34bddd14824117f9836f25073_1440w.jpg)

除了老牌的 LangChain 和 LangGraph，Vercel AI SDK、Claude Agent SDK、Pydantic AI 的使用人数是最多的。

关于技术选型，我也让 Claude Code 做了个简单总结：

![技术选型](assets/ai-agent-frameworks-comparison/v2-bd7ce7efa1d4b01bbc1fac0e7df0a6d5_1440w.jpg)

如果是个人项目，想快速上手，可以选择 pi-mono(Pi)；如果想开发 Web 端的 AI Agent，可以选择 Vercel AI SDK；如果想开发一个类似 Claude Code 的复杂 Agent，或者企业级的应用，可以选择 Claude Agent SDK 或者 LangChain/LangGraph。另外如果是 Python 开发者，想快速开发，可以选 Pydantic AI。

### 主流框架

#### LangChain 和 LangGraph

LangChain 和 LangGraph 都是 LangChain 官方开发的框架，前者出现得更早，大概是在 2022 年，而后者大概是在2024 年诞生的。

LangChain 顾名思义，旨在通过"链式"组合来简化大语言模型（LLM）应用的开发，像早期的 AI 聊天机器人，就通常用 LangChain 来开发。

不过由于 LangChain 是"链式"的线性逻辑，比较难处理需要循环逻辑和复杂状态管理的智能体。为了解决这些痛点，LangChain 官方推出了 LangGraph 作为 LangChain 的扩展库。

相比 LangChain，LangGraph 可以实现复杂的流程编排（循环/分支/重试），支持多智能体协作，支持并行任务，方便实现人机交互。

LangGraph 也是 LangChain 官方目前首推的 Agent 开发框架。不过 LangGraph 通常会和 LangChain 搭配起来使用。如果场景比较简单，LangChain 也够用。

具体如何选择，建议看看官方文档：https://docs.langchain.com/oss/python/langgraph/overview

![LangGraph](assets/ai-agent-frameworks-comparison/v2-6a55a5fd657fedb7ae3bcdaf67e596aa_1440w.jpg)

需要注意的是，LangChain 和 LangGraph 诞生得比较早，但由于概念比较多，且 LangGraph 是偏底层（low-level）的框架，学习成本会比较高。

#### Claude Agent SDK

注意，Claude Agent SDK 虽然有 Github 地址，但并没有真正开源，核心逻辑打包成二进制文件了。但由于用的人不少，还是介绍一下。

Claude Agent SDK 最早叫 Claude Code SDK，因为能力越来越通用，最近才改了名字。

从它原来的名字（Claude Code SDK）就可以看出，Claude Agent SDK 诞生自 Claude Code，包含了 Claude Code 的底层核心能力。

就像官方文档说的，Claude Agent SDK 能让你快速开发一个类似 Claude Code 的 AI Agent。

![Claude Agent SDK](assets/ai-agent-frameworks-comparison/v2-5faf6352c605ad83cfeffe59f6ad1317_1440w.jpg)

Claude Code 的强大应该是有目共睹的，它的工程架构设计非常优秀。

使用 Claude Agent SDK 开发 AI Agent，是非常不错的一个选择，由于 SDK 抽象程度比较高，上手成本低，能够比较快地开发一个功能完备的 AI Agent。

不过 Claude Agent SDK 的母公司 Anthropic 对咱们不太友好，如果你没有一个纯净的代理，官方文档都访问不了。

官方文档：https://platform.claude.com/docs/zh-CN/agent-sdk/overview

![官方文档](assets/ai-agent-frameworks-comparison/v2-9de5d08730d5f170648f621aa14b63e8_1440w.jpg)

好在代码仓库是开源的，可以让 AI 学习仓库内容，然后帮你编写相关代码。

- Python SDK：https://github.com/anthropics/claude-agent-sdk-python
- TypeScript SDK：https://github.com/anthropics/claude-agent-sdk-typescript

另外 Claude Agent SDK 和 Anthropic 的 Claude 系列模型搭配起来，效果会比较好。

如果要使用其他模型，通常需要该模型兼容了 Anthropic API 格式（比如 GLM-4.7、GLM-5.0），或者使用 LiteLLM 等方式来桥接，但效果大概率都不如 Claude Agent SDK + Claude。

但想在国内稳定用上 Claude 也是一件难事。在国内非要用的话，Claude Agent SDK + GLM（或者其他兼容模型）是一个可行的方案。

#### Vercel AI SDK

从 Github Star 数和 npm 包下载量看来，Vercel AI SDK 比 Claude Agent SDK 更受欢迎一些。

Vercel 这家公司也挺有名的，它旗下最著名的产品，一个是 Next.js 全栈框架，一个是 Vercel 这个网站托管平台。如果你想在海外免费部署一个网站，通常会在 Vercel 和 Cloudflare 里二ercel 还是挺选一。

V厉害的，不知道怎么把 ai 这个 npm 包弄到手了，作为 Vercel AI SDK 的包名。以至于看着就很牛逼的样子。

![Vercel AI SDK](assets/ai-agent-frameworks-comparison/v2-ccef3aa8a0021b9d283e8f1184442374_1440w.jpg)

Vercel AI SDK 和 Claude Agent SDK 的能力大差不差，前者的优势主要在于多模型的支持，以及和 Vercel 自身生态的适配。

| 功能维度 | Claude Agent SDK | Vercel AI SDK | 关键说明 |
|---|---|---|---|
| Claude 模型调用（含 Code） | ✅ 原生全支持 | ✅ 全支持 | Vercel AI SDK 封装了anthropic-sdk，无调用限制，参数透传完整 |
| 多轮对话状态管理 | ✅ 需手动管理消息历史 | ✅ 更简化 | Vercel AI SDK 内置useChat/createAnthropicChatCompletion，无需手动拼接 |
| 工具调用（Tool Use） | ✅ 原生支持 Claude 工具调用协议 | ✅ 需适配 | Vercel AI SDK 无原生封装，但可自定义实现 Claude 的工具调用逻辑 |
| 流式响应（Stream） | ✅ 原生支持 | ✅ 深度优化 | Vercel AI SDK 对前端 / Edge 流式渲染更友好（如 React Hooks、分块输出） |
| Claude 专属参数透传 | ✅ 原生支持 | ✅ 间接支持 | 可在 Vercel AI SDK 中手动透传 Claude 专属参数（如max_tokens/temperature） |
| Anthropic 企业级功能 | ✅ 支持（企业版） | ❌ 暂不支持 | 如 Claude 私有部署、模型微调（Fine-tuning）、企业级权限管控 |
| 多模型适配 | ❌ 仅支持 Claude 系列（或兼容 API 模型） | ✅ 全支持 | 一套代码适配 Claude/OpenAI/Gemini/Mistral 等，Claude SDK 无此能力 |
| Vercel 生态集成 | ❌ 无 | ✅ 原生支持 | 与 Next.js/Edge Functions/KV 存储无缝协同，部署到 Vercel 云零配置 |
| 本地运行 | ✅ 支持 | ✅ 支持 | 二者均无需依赖云端，可本地运行 Agent 逻辑 |

由于 Vercel AI SDK 和 Next.js、React、Vue 等全栈和前端框架的适配比较好，很适合用于构建 Web AI 应用。比如在你的网站里添加一个 AI 智能助手。

当然 Vercel AI SDK 也可以用于开发类似 Claude Code 的本地 AI Agent 应用。

目前 Vercel AI SDK 官方的 SDK 是 TypeScript 的，虽然也提供了 Python 版的 SDK，但用的人好像不多。

- TypeScript：https://github.com/vercel/ai
- Python SDK：https://github.com/python-ai-sdk/sdk

综合受欢迎程度（使用人数）、学习门槛、开发效率等因素，Vercel AI SDK 几乎可以说是新手开发 AI Agent 应用的最佳选择。

#### pi-mono(Pi)

pi-mono（简称 Pi）是一个追求极简主义的 AI Agent 开发框架，前些时大火的 OpenClaw（原 ClawBot），就是基于 Pi 开发的。

伴随着 OpenClaw 的大火，pi-mono 一下子受到了很多人的关注，Star 数也在这段时间激增。

![pi-mono](assets/ai-agent-frameworks-comparison/v2-8df6ceca569f42184fa42a59583ce250_1440w.jpg)

相比前面介绍的 LangGraph、Claude Agent SDK 和 Vercel AI SDK，Pi 就小很多，支持的能力也不算完善，比如常见的 MCP、多智能体、子代理、Computer Use，Pi 都没有内置支持。

![Pi能力对比](assets/ai-agent-frameworks-comparison/v2-1a7aa64c6683c1d8dcf1396c23b40806_1440w.jpg)

举个不那么恰当的例子，当大家都在用 Unity、Godot 等游戏引擎开发游戏时，小丑牌的作者用的是 love2d 这个极简的 lua 框架。Pi 就好比 love2d 这个框架。

麻雀虽小，但 Pi 重在简单，概念很少，学习成本算是众多框架中最低的。

另外虽然 Pi 没有内置 MCP、子代理、Plan Mode 等能力，但可以通过扩展来实现这些能力，官方也提供了对应的例子。

![Pi扩展](assets/ai-agent-frameworks-comparison/v2-455805c99ddf2b945f114f634a51a360_1440w.jpg)

目前 Pi 只提供了 TypeScript 的 SDK：https://github.com/badlogic/pi-mono。看来 AI 时代，多少得学点 TS 了。

#### Pydantic AI

熟悉 Python 的朋友应该都知道 Pydantic 这个库。

Pydantic 是 Python 中最主流的数据验证与结构化库（2017 年推出，v2 版本用 Rust 重写，性能提升 10-50 倍），核心使命是解决 Python 动态类型带来的"数据不可靠、参数校验繁琐"等问题。

而 Pydantic AI 是官方基于 Pydantic 核心能力构建的 AI Agent 开发框架。

如果你对 Pydantic 和 Python 比较熟，那 Pydantic AI 可能是你的最佳选择。我看 X 上也有不少人在评论区推荐。

仓库地址：https://github.com/pydantic/pydantic-ai

![Pydantic AI](assets/ai-agent-frameworks-comparison/v2-ec8681ddcfeea08691333a94fbb7446b_1440w.jpg)

从 Github 上的 Star 数看，Pydantic AI 也挺受欢迎的（虽然增长趋势不及另两位）。

从最前面的概览部分也能看出，以周下载量来看，在支持 Python 的 AI Agent 框架里，Pydantic AI 能排到前三名（LangChain > LangGraph > Pydantic）。

内置能力上，基本该有的都有，具体可以参考官方文档：https://ai.pydantic.dev/。

#### Google ADK

Google 的 ADK，全称是 Agent Development Kit，是一个功能完备的 Agent 开发工具包。

![Google ADK](assets/ai-agent-frameworks-comparison/v2-a3e01a1661ba903762236a274497a94c_1440w.jpg)

毕竟是 Google 出品，质量还是很有保障的。相比 Claude Agent SDK，ADK 从设计上就是模型无关的，能够兼容绝大多数模型。

另外，ADK 是唯一一个同时支持 Python/TypeScript/Go/Java 四种语言的 Agent 开发框架。单从 npm 和 PyPI 上的下载量来看，每周也有 90 多万（npm 23K + PyPI 908K）的下载量，以 Python SDK 为主。

Claude Agent SDK 和 Vercel AI SDK 支持的，Google ADK 都支持，包括但不限于代码执行、Google 搜索、上下文缓存、Computer Use、交互 API 等等。

Google ADK 最主要的优势在于能很好的和 Google 生态做集成。比如无缝对接 Gemini 模型，支持原生多模态能力。再比如 ADK 深度整合了 Google Cloud、Google Workspace（如 Docs/Sheet/Slides）等产品，可以直接调用。

另外也提供了企业级的安全合规功能。

| 对比维度 | Google ADK | Claude Agent SDK | Vercel AI SDK |
|---|---|---|---|
| 核心定位 | 企业级全栈 Agent 开发套件 | Claude 专属轻量 Agent SDK | 多模型通用 AI 交互 / 流式 SDK |
| 模型支持 | 绝大多数 | Claude 以及兼容 Claude API 的模型 | 全平台通吃：Claude / GPT / Gemini |
| 多模态能力 | 原生最强（文本、代码、图片、音频、视频） | 支持，但需手动处理 | 依赖底层模型，无原生封装 |
| 生态集成 | GCP、Workspace、Google 搜索全打通 | 仅 Anthropic 生态 | Vercel / Next.js/ 前端生态 |
| 企业级能力 | 极强：IAM、合规、审计、私有部署 | 弱，仅企业版少量支持 | 几乎没有 |
| 本地 / 离线部署 | 支持：云端 / 边缘 / 离线（Gemini Nano） | 不支持，必须走云端 API | 仅本地逻辑，模型仍需云端 |
| 前端 & 部署体验 | 差，无前端封装 | 差，纯后端 | 极强：React Hooks、流式、一键部署 |
| 学习成本 | 高（要懂 GCP 生态） | 低（直接用 Claude） | 低（JS/TS 前端友好） |
| 最适合场景 | 企业、内网离线、多模态、Google 生态 | 纯 Claude Code Agent、个人轻量 | 快速 Demo、前端优先、多模型切换 |

Google ADK 整体来看还是比较全面的，不过像这种大而全的框架，学习成本通常要更高一些，如果要和 Google 生态做深度集成，还是需要一些相关领域知识的。

另外 Google ADK 和 Google 生态深度整合的能力，在国内不怎么用得到。可能更适合外海或者出海企业。

- 相关文档：Agent Development Kit (ADK)
- 相关仓库：https://github.com/google?q=adk

#### AWS Strands Agents

无论是从 Star 数还是下载量来看，AWS 的 Strands Agents 相对就比较小众了。我还是刷 X 看到的这个框架。

- https://github.com/strands-agents/sdk-python
- https://github.com/strands-agents/sdk-typescript

我简单看了下 Github 上的文档，发现 Strands Agents 的 API 设计得挺简洁的，它的 README 中也强调，Strands Agents 是一款简单却功能强大的 SDK，号称用几行代码就可以构建一个 AI Agent。

![Strands Agents](assets/ai-agent-frameworks-comparison/v2-375a937f27de27dd6c061bb73afb7b28_1440w.jpg)

当然 Strands Agents 的优势其实和 Google ADK 有点类似，一个是模型无关（支持多个模型和模型提供商），一个是能很好地和 AWS 生态做集成。

| 对比维度 | Strands Agents | Google ADK |
|---|---|---|
| 出品方 & 生态根基 | AWS 主导，原生深度绑定 AWS 全栈：Bedrock、AgentCore、Lambda、Step Functions、IAM 等 | Google 主导，深度融合 Google 生态：GCP、Vertex AI、Gemini、Workspace、搜索、Gemini Nano |
| 设计哲学 | 模型驱动（Model-Driven）：极简开发，用 prompt+tools 两行代码定义 Agent；把规划、工具选择、反思交给模型自主决策 | 模块化 / 代码优先：像写传统软件那样构建 Agent；分层架构、显式流程控制；提供确定性编排原语 |
| 协议优先级 | MCP 第一优先级：原生 MCP，标准化工具上下文；A2A 支持但非核心定位 | A2A 原生 + MCP 兼容：Google 主导 A2A 协议，MCP 用于工具集成 |
| 部署场景 | 本地 (Ollama)+AWS 全栈；适合 AWS 混合云 | GCP + 边缘 + 离线三位一体；支持 Gemini Nano 设备端部署 |
| 多模态能力 | 依赖底层模型；无 Google 级原生多模态封装 | 原生 Google 多模态最强：内置支持文本、图像、音频、视频 |
| 语言支持 | Python/TypeScript | Python/TS/Go/Java |
| 上手门槛 | 中低；模型驱动，代码极简 | 中高；模块化架构、显式流程控制 |
| 安全合规 | 绑定 AWS 安全体系：IAM、Bedrock Guardrails | 绑定 Google 企业安全：IAM、VPC |

对 Strands Agents 有兴趣的朋友可以去官网看看文档：https://strandsagents.com/latest/documentation/docs/。

### 如何选型

其实前面介绍得差不多了，最后让 AI 帮我总结了一下，基本符合当前社区的共识。

![选型建议1](assets/ai-agent-frameworks-comparison/v2-2f9a510d99fa18f02bff8be0bed685ac_1440w.jpg)

![选型建议2](assets/ai-agent-frameworks-comparison/v2-634fc11d1a2b366c0d2a83e3e3ff38c5_1440w.jpg)

我再废话归纳下。

如果想快速学习和了解 AI Agent 开发，可以看看 pi-mono 或者 Vercel AI SDK。 如果是要开发真实的应用，那就要具体情况具体分析了。

比如你想充分掌控细节，一切从零开始，那可以选择老牌的 LangChain/LangGraph。 如果你想快手开发，那 Vercel AI SDK 和 Claude Agent SDK 可能更适合你。 如果你是出海或者海外企业，服务部署在谷歌云或者 AWS 上，需要和 Google 或者 AWS 生态做集成，那可以考虑 Google ADK 或 AWS Strands Agents。 另外如果你的团队都是写 Python 的，那 Pydantic AI 是个不错的选择。

再比如你在国内，要构建企业级的 AI Agent，除了上面的这些框架，还可以考虑使用国内云厂商的一些方案，比如火山引擎的 AgentKit。

另外评论区还提到了 Agno（Python）和 Mastra（TS）这两个框架，用的人也不少，感兴趣的朋友可以调研下。

最后，大家如果有相关经验，比如使用这些框架或者开发 AI Agent 的真实体验，也可以分享到评论区，让我们一起学习学习。
