# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## ClawHub 账号

- **账号**：ramyun@163.com
- **密码**：Dtrfgd45
- **Token**：clh_EAvXynxaaqpsKiBOggBe3XvjAhsIQm22F3qBo3fdQLM

---

## 已安装技能清单 (2026-03-14 更新)

### 核心能力
| 技能 | 功能 | 安装状态 |
|------|------|----------|
| **self-improving-agent** | 自我进化，记录错误和经验 | ✅ 已安装 |
| **brave-search** | 轻量级网页搜索 | ✅ 已安装 |
| **github** | GitHub CLI管理 | ✅ 已安装 |
| **akshare-stock** | A股量化数据分析 | ✅ 已安装 |
| **automation-workflows** | 自动化工作流(n8n/Zapier) | ✅ 已安装 |

### 股票分析
| 技能 | 功能 | 安装状态 |
|------|------|----------|
| **tavily** | AI优化搜索 | ✅ 已安装 |
| **multi-search-engine** | 多引擎聚合 | ✅ 已安装 |
| **stock-research-engine** | 个股深度研究 | ✅ 已安装 |
| **stock-monitor-skill** | 智能监控预警 | ✅ 已安装 |
| **stock-screener-cn** | A股技术筛选 | ✅ 已安装 |

### 内容创作
| 技能 | 功能 | 安装状态 |
|------|------|----------|
| **ai-news-collectors** | AI新闻聚合 | ✅ 已安装 |
| **daily-report** | 日报生成 | ✅ 已安装 |
| **md-to-pdf** | Markdown转PDF | ✅ 已安装 |

### 系统工具
| 技能 | 功能 | 安装状态 |
|------|------|----------|
| **channels-setup** | IM通道配置 | ✅ 已安装 |

---

## Self-Improving-Agent 配置

### 学习记录目录
```
~/.openclaw/workspace/.learnings/
├── LEARNINGS.md      # 学习记录
├── ERRORS.md         # 错误记录
└── FEATURE_REQUESTS.md # 功能请求
```

### 使用触发
- 命令失败时 → 记录到 ERRORS.md
- 用户纠正时 → 记录到 LEARNINGS.md
- 发现更好方法 → 记录到 LEARNINGS.md

---

Add whatever helps you do your job. This is your cheat sheet.
