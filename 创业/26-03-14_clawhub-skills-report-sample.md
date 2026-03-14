# ClawHub 热门技能推荐报告
**报告时间**：2026年3月14日  
**数据来源**：ClawHub 官方市场 + 社区实测推荐

---

## 📊 今日技能榜单（按下载量/实用性排序）

### 🥇 必装基础技能（优先级：最高）

| 技能名称 | 作者 | 核心功能 | 适用场景 | 安装命令 |
|---------|------|---------|---------|---------|
| **Tavily Search** | arun-8687 | AI专用实时联网搜索 | 新闻追踪、市场调研 | `clawhub install arun-8687/tavily-search` |
| **Self-Improving Agent** | - | 自我进化、经验沉淀 | 长期使用、个性化优化 | `clawhub install self-improving-agent` |
| **Find Skills** | - | 技能导航、智能推荐 | 快速找工具 | `clawhub install find-skills` |
| **Summarize** | - | 长文本/视频总结 | 研报、文章速读 | `clawhub install summarize` |
| **Agent Browser** | - | AI操控浏览器 | 自动爬取、网页操作 | `clawhub install agent-browser` |

---

### 📈 金融投资类（忠哥重点关注）

| 技能名称 | 作者 | 核心功能 | 安装命令 |
|---------|------|---------|---------|
| **AkShare Stock** | mbpz | A股量化数据、行情分析 | `clawhub install mbpz/akshare-stock` |
| **Stock Watcher** | - | 自选股管理、价格预警 | `clawhub install stock-watcher` |
| **US Stock Analysis** | - | 美股基本面分析、估值 | `clawhub install us-stock-analysis` |
| **Multi Search Engine** | - | 17个搜索引擎聚合 | `clawhub install multi-search-engine` |

**金融组合用法示例**：
```
1. Tavily Search → 搜华胜天成最新动态
2. AkShare Stock → 查财务数据、技术指标
3. Stock Watcher → 设价格预警（如跌破27元提醒）
4. Summarize → 自动总结研报和新闻
```

---

### 💼 办公自动化类

| 技能名称 | 核心功能 | 安装命令 |
|---------|---------|---------|
| **gog** | Google全家桶（Gmail/日历/Drive） | `clawhub install gog` |
| **feishu-doc** | 飞书文档读写 | `clawhub install feishu-doc` |
| **feishu-calendar** | 飞书日历管理 | `clawhub install feishu-calendar` |
| **nano-pdf** | PDF编辑、合并、提取 | `clawhub install nano-pdf` |
| **meeting-minute-taker** | 会议纪要自动生成 | `clawhub install meeting-minute-taker` |
| **Office-Automation** | 邮件/日程/文档自动化 | `clawhub install office-automation` |

---

### 🔧 开发运维类

| 技能名称 | 核心功能 | 安装命令 |
|---------|---------|---------|
| **GitHub** | PR管理、Issue追踪 | `clawhub install github` |
| **GitLab** | 代码仓库操作 | `clawhub install gitlab` |
| **Vercel** | 部署管理 | `clawhub install vercel` |
| **NeonDB** | 数据库操作 | `clawhub install neondb` |
| **Code Review** | 自动代码审查 | `clawhub install code-review` |

---

### 📰 信息获取类

| 技能名称 | 核心功能 | 安装命令 |
|---------|---------|---------|
| **AI News Collectors** | kenxcomp | 每日新闻简报 | `clawhub install kenxcomp/ai-news-collectors` |
| **Union Search** | runningZ1 | 跨平台搜索（B站/抖音/小红书等） | 需GitHub克隆 |
| **Exa Search** | - | 语义搜索 | `clawhub install exa-search` |

---

### 🎨 内容创作类

| 技能名称 | 核心功能 | 安装命令 |
|---------|---------|---------|
| **xiaohongshu-mcp** | Borye | 小红书全自动运营 | `clawhub install Borye/xiaohongshu-mcp` |
| **wechat-mp-writer** | hahacatlsq | 公众号自动写作 | `clawhub install hahacatlsq/wechat-mp-writer-skill-mxx` |
| **chirp** | zizi-cat | X/Twitter自动运营（浏览器版） | `clawhub install zizi-cat/chirp` |
| **x-twitter** | annettemekuro30 | X官方API版 | `clawhub install annettemekuro30/x-twitter` |
| **ElevenLabs** | - | 文字转语音/声音克隆 | `clawhub install elevenlabs` |
| **fal-ai** | - | AI图像生成 | `clawhub install fal-ai` |

---

### 📝 知识管理类

| 技能名称 | 核心功能 | 安装命令 |
|---------|---------|---------|
| **Notion** | 云端笔记自动化 | `clawhub install notion` |
| **Obsidian** | 本地笔记双向链接 | `clawhub install obsidian` |
| **PDF Parser** | PDF内容提取 | `clawhub install pdf-parser` |
| **PPTX** | PPT生成/解析 | `clawhub install pptx` |

---

### 🔄 工作流自动化

| 技能名称 | 核心功能 | 安装命令 |
|---------|---------|---------|
| **Clawflows** | 流程编排 | `clawhub install clawflows` |
| **Mission Control** | 任务调度 | `clawhub install mission-control` |
| **Personal Assistant** | 个人助理（带记忆） | `clawhub install personal-assistant` |
| **Remind Me** | 提醒事项 | `clawhub install remind-me` |
| **Todo Tracker** | 待办管理 | `clawhub install todo-tracker` |

---

## 🎯 新手推荐安装顺序

**第一步：基础能力（5个）**
```bash
clawhub install find-skills tavily-search summarize agent-browser self-improving-agent
```

**第二步：办公效率（按需）**
```bash
# 飞书用户
clawhub install feishu-doc feishu-calendar

# Google用户
clawhub install gog

# PDF处理
clawhub install nano-pdf
```

**第三步：金融投资（忠哥专用）**
```bash
clawhub install mbpz/akshare-stock stock-watcher multi-search-engine
```

**第四步：内容创作（可选）**
```bash
clawhub install xiaohongshu-mcp wechat-mp-writer chirp
```

---

## 📌 今日技能更新动态

- ClawHub 当前收录 **400+** 社区技能
- 新增技能：金融分析类、办公自动化类持续增加
- 热门趋势：自我进化类技能（Self-Improving Agent）安装量突破 46,000+

---

## ⚠️ 安装注意事项

1. **部分技能需额外配置API Key**（如 Tavily、股票类）
2. **登录 ClawHub 后再安装**：`clawhub login --token <你的token>`
3. **安装失败重试**：网络不稳定时多试几次
4. **查看文档**：每个技能页面有详细使用说明

---

*报告生成时间：2026-03-14 05:15*  
*下次更新时间：每日 12:00*
