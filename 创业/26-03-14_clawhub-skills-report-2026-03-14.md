# ClawHub 热门技能推荐报告（2026年3月14日）

> 报告日期：2026年3月14日  
> 数据来源：ClawHub官方市场、OpenClaw社区、各大技术博客及券商研报  
> 技能总数：ClawHub市场已收录 **13,729+** 个社区技能

---

## 📊 今日市场动态概览

### 生态热点
- **OpenClaw** GitHub星标数突破 **28万**，持续霸榜趋势
- **火山引擎ArkClaw**正式上线，10000+技能开箱即用
- **WPS 365**接入OpenClaw数字员工，办公自动化能力升级
- 券商研报密集发布：华创、国金、东吴等券商均发布OpenClaw金融投研应用指南

### 用户关注点
| 排名 | 关注领域 | 占比 | 热门技能示例 |
|------|----------|------|--------------|
| 1 | 金融投资类 | 35% | Stock-Watcher、Market-Pro、Stock-Analysis |
| 2 | 办公自动化类 | 30% | GOG、Office-Automation、Excel-Wizard |
| 3 | 信息获取类 | 20% | Tavily、Multi-Search、Agent-Browser |
| 4 | 安全工具类 | 15% | Skill-Vetter、Exec-Guard |

---

## 🔍 一、信息获取类技能

### 1. Tavily Search（AI搜索神器）
| 属性 | 详情 |
|------|------|
| **技能名称** | tavily-search |
| **作者** | steipete / tavily |
| **下载量** | 98.3K+ |
| **核心功能** | 专为AI Agent优化的搜索API，返回结构化结果，无广告干扰。支持自定义搜索深度、结果数量、域名过滤，内置5分钟缓存机制 |
| **适用场景** | 实时查论文、新闻、产品价格、航班信息；打破AI"信息孤岛" |
| **安装命令** | `clawhub install tavily-search` |
| **配置要求** | 需注册Tavily账号获取API Key：`clawhub config set TAVILY_API_KEY <your-key>` |

**实战示例**：
```
"搜索2026年AI医疗市场规模最新数据，给出结构化报告"
```

---

### 2. Multi Search Engine（全网搜索聚合器）
| 属性 | 详情 |
|------|------|
| **技能名称** | multi-search-engine |
| **作者** | community |
| **核心功能** | 集成17个搜索引擎（8个国内+9个国际），无需API Key即可使用。支持多源对比验证、隐私搜索、知识计算 |
| **适用场景** | 深度调研、信息交叉验证、隐私保护搜索、数学计算 |
| **安装命令** | `clawhub install multi-search-engine` |
| **特色引擎** | 百度、谷歌、必应、DuckDuckGo、WolframAlpha |

**实战示例**：
```
"用multi-search-engine搜索'中东局势对原油市场的影响'，整合多引擎结果交叉验证"
```

---

### 3. Agent Browser（浏览器自动化）
| 属性 | 详情 |
|------|------|
| **技能名称** | agent-browser |
| **作者** | openclaw-community |
| **下载量** | 117K+ |
| **核心功能** | 让AI直接操控浏览器，支持网页数据采集、自动化操作、表单填写。Rust编写，性能优异 |
| **适用场景** | Web自动化、数据采集、AI驱动的网页交互 |
| **安装命令** | `clawhub install agent-browser` |
| **技术亮点** | Rust核心+Node.js fallback，跨平台兼容 |

---

### 4. Find Skills（技能导航仪）
| 属性 | 详情 |
|------|------|
| **技能名称** | find-skills |
| **作者** | community |
| **下载量** | 185K+ |
| **核心功能** | 自然语言提问，精准匹配ClawHub上的技能。ClawHub生态的"导航员" |
| **适用场景** | 新手快速找技能、批量管理已安装技能 |
| **安装命令** | `clawhub install find-skills` |

---

### 5. Summarize（智能摘要）
| 属性 | 详情 |
|------|------|
| **技能名称** | summarize |
| **作者** | openclaw-community |
| **下载量** | 142K+ |
| **核心功能** | 支持网页/PDF/图片/音频/YouTube全格式摘要。4种摘要模式：bullet要点/executive管理层/detailed详细/action-items待办 |
| **适用场景** | 长文速读、会议纪要、研报提炼 |
| **安装命令** | `clawhub install summarize` |

---

## 💰 二、金融投资类技能

### 1. Stock-Analysis（股票分析）
| 属性 | 详情 |
|------|------|
| **技能名称** | stock-analysis |
| **作者** | financial-ai-team |
| **下载量** | 84.6万+ |
| **核心功能** | 美股/A股基本面分析、技术分析、投资报告生成。支持实时股价追踪、加密货币行情、DCF估值建模 |
| **适用场景** | 个股深度研究、早盘报告生成、量化策略构建 |
| **安装命令** | `clawhub install stock-analysis` |
| **前置条件** | 需配置LF Financial Analysis API Key |

**实战示例**：
```
"用stock-analysis分析贵州茅台（600519）的最新财务数据，生成DCF估值报告"
```

---

### 2. Stock-Watcher（股票盯盘）
| 属性 | 详情 |
|------|------|
| **技能名称** | stock-watcher |
| **作者** | clawdbot |
| **下载量** | 68.4万+ |
| **核心功能** | 实时价格异动监控、自选股管理、价格预警提醒。数据源：东方财富、新浪财经等 |
| **适用场景** | 个股盯盘、持仓监控、预警提醒 |
| **安装命令** | `clawhub install stock-watcher` |

**实战示例**：
```
"用Stock-Watcher添加贵州茅台（600519）到观察列表，设置跌破1600元触发提醒"
```

---

### 3. Stock-Market-Pro（股市分析专业版）
| 属性 | 详情 |
|------|------|
| **技能名称** | stock-market-pro |
| **作者** | pro-traders |
| **核心功能** | 本地优先的股市工具，输入股票代码直接生成RSI/MACD/布林带等技术指标高清图表 |
| **适用场景** | 技术分析、图表生成、走势对比 |
| **安装命令** | `clawhub install stock-market-pro` |

**实战示例**：
```
"分析贵州茅台（600519）的技术指标，生成高清图表和分析报告"
```

---

### 4. QVeris（A股数据接入）
| 属性 | 详情 |
|------|------|
| **技能名称** | qveris-official |
| **作者** | qveris.ai |
| **核心功能** | 专业A股数据接口，支持实时行情、龙虎榜、涨停分析、定时任务监控 |
| **适用场景** | A股实时监控、量化选股、自动报告生成 |
| **安装命令** | `clawhub install qveris-official` |
| **配置要求** | 需QVeris API Key |

**实战示例**：
```
"每15分钟查看并分析A股涨跌幅度较大的股票，推送潜力股推荐"
```

---

### 5. Market-Data-Fetch（行情数据抓取）
| 属性 | 详情 |
|------|------|
| **技能名称** | market-data-fetch |
| **作者** | data-team |
| **核心功能** | 抓取A股/美股/港股全球市场OHLCV数据，支持实时行情与历史K线，自动数据清洗 |
| **适用场景** | 量化研究、数据回测、策略开发 |
| **安装命令** | `clawhub install market-data-fetch` |
| **数据源** | Tushare、Yahoo Finance等 |

---

### 6. Yahoo Finance（雅虎财经）
| 属性 | 详情 |
|------|------|
| **技能名称** | yahoo-finance |
| **作者** | yahoo-finance-team |
| **下载量** | 73.2万+ |
| **核心功能** | 获取股票价格、基本面、股息、分析师评级，无需API密钥 |
| **适用场景** | 美股查询、基本面分析 |
| **安装命令** | `clawhub install yahoo-finance` |

---

## 🏢 三、办公自动化类技能

### 1. GOG（Google Workspace集成）
| 属性 | 详情 |
|------|------|
| **技能名称** | gog |
| **作者** | google-workspace-team |
| **下载量** | 85.4K+ |
| **核心功能** | 一键集成Gmail、Google Calendar、Google Docs、Google Sheets。邮件自动分类、日程智能安排、文档协同编辑 |
| **适用场景** | 邮件管理、日程协调、文档处理 |
| **安装命令** | `clawhub install gog` |

**实战示例**：
```
"每天早上8点自动扫描邮件，提取重要邮件摘要，同步到日历"
```

---

### 2. Office-Automation（办公自动化神器）
| 属性 | 详情 |
|------|------|
| **技能名称** | office-automation |
| **作者** | office-ai-team |
| **核心功能** | Excel处理、报告生成、邮件发送、日程管理。覆盖数据处理、文档生成、批量整理全场景 |
| **适用场景** | 周报生成、数据处理、批量文件整理 |
| **安装命令** | `clawhub install office-automation` |

**实战示例**：
```
"用office-automation生成本周工作周报，从运营数据.xlsx提取数据，生成PDF发送到团队邮箱"
```

---

### 3. Excel Wizard（Excel魔法师）
| 属性 | 详情 |
|------|------|
| **技能名称** | excel-wizard |
| **作者** | excel-ai-team |
| **核心功能** | 直接操作本地Excel文件，支持跨表数据合并、清洗、图表生成。非简单公式生成器 |
| **适用场景** | 销售数据分析、财务报表处理、数据可视化 |
| **安装命令** | `clawhub install excel-wizard` 或 `openclaw skill install excel-wizard` |

**实战示例**：
```
"合并三个季度的销售表，生成环比增长柱状图，15秒出结果"
```

---

### 4. DocAssistant Pro（文档助手专业版）
| 属性 | 详情 |
|------|------|
| **技能名称** | doc-assistant-pro |
| **作者** | doc-ai-team |
| **核心功能** | Word/PDF智能排版、合同条款比对、批量格式转换。强项"结构化提取"，可从200份简历精准提取学历和期望薪资 |
| **适用场景** | 长文档处理、合同审查、批量简历筛选 |
| **安装命令** | `clawhub install doc-assistant-pro` 或 `openclaw skill install doc-assistant-pro` |

---

### 5. MailButler（邮件管家）
| 属性 | 详情 |
|------|------|
| **技能名称** | mail-butler |
| **作者** | email-ai-team |
| **核心功能** | 接管SMTP/IMAP，智能分类邮件、依据上下文起草回复。最强功能"截止日期嗅探"，自动识别隐蔽Deadline并加入日历 |
| **适用场景** | 邮件管理、自动回复、日程同步 |
| **安装命令** | `clawhub install mail-butler` 或 `openclaw skill install mail-butler` |

---

### 6. Notion（知识管理）
| 属性 | 详情 |
|------|------|
| **技能名称** | notion |
| **作者** | notion-team |
| **下载量** | 40.9K+ |
| **核心功能** | 读写Notion工作区，自动创建笔记、管理数据库、同步任务 |
| **适用场景** | 知识库管理、项目协作、个人笔记 |
| **安装命令** | `clawhub install notion` |

---

### 7. N8N Workflow Automation（工作流编排）
| 属性 | 详情 |
|------|------|
| **技能名称** | n8n-workflow-automation |
| **作者** | n8n-team |
| **核心功能** | 开源自动化工具，让OpenClaw直接调用n8n节点，实现跨App联动 |
| **适用场景** | 邮件来了自动存到Notion、触发Zapier通知、更新Trello卡片 |
| **安装命令** | `clawhub install n8n-workflow-automation` |

---

## 🛡️ 附：安全类必装技能

### 1. Skill Vetter（安全扫描）
| 属性 | 详情 |
|------|------|
| **技能名称** | skill-vetter |
| **作者** | security-team |
| **核心功能** | 安装其他技能前扫描代码，检测恶意程序，规避安全风险 |
| **适用场景** | 所有技能安装前的安全检查 |
| **安装命令** | `clawhub install skill-vetter` |

---

### 2. Self-Improving Agent（自我迭代）
| 属性 | 详情 |
|------|------|
| **技能名称** | self-improving-agent |
| **作者** | pskoett |
| **下载量** | 117K+ / 46K+（不同来源统计） |
| **核心功能** | 让Agent记住错误与成功经验，自动复盘优化，越用越聪明 |
| **适用场景** | 长期重复工作、持续优化输出质量 |
| **安装命令** | `clawhub install self-improving-agent` |
| **ClawHub地址** | clawhub.ai/pskoett/self-improving-agent |

---

## 📈 安装推荐组合

### 新手入门组合（5个）
```bash
# 安全+基础能力
clawhub install skill-vetter tavily-search summarize find-skills

# 办公必备
clawhub install office-automation
```

### 金融投资者组合（8个）
```bash
# 股票分析套件
clawhub install stock-watcher stock-analysis market-data-fetch yahoo-finance

# 辅助工具
clawhub install tavily-search multi-search-engine summarize report-generator
```

### 办公自动化组合（6个）
```bash
# 办公套件
clawhub install gog office-automation excel-wizard doc-assistant-pro mail-butler

# 效率工具
clawhub install notion
```

### 全能组合（12个）
```bash
# 一站式安装
clawhub install skill-vetter tavily-search multi-search-engine summarize \
  stock-watcher stock-analysis gog office-automation excel-wizard \
  find-skills self-improving-agent agent-browser notion
```

---

## ⚠️ 重要提示

1. **安全第一**：安装任何技能前，建议先安装`skill-vetter`进行安全扫描
2. **API Key管理**：涉及金融数据、搜索等技能需配置API Key，请妥善保管
3. **风险提示**：金融Skill分析结果仅供参考，不构成投资建议
4. **定期更新**：关注ClawHub官方更新，及时升级技能版本

---

## 📚 参考资源

- **ClawHub官方市场**：https://clawhub.ai
- **OpenClaw GitHub**：https://github.com/openclaw/openclaw
- **社区推荐**：https://github.com/openclaw-commons/openclaw-skill-commons
- **券商研报**：华创证券《OpenClaw金融行业必备Skills推荐》、国金证券《AI智能体投研应用指南》

---

*报告生成时间：2026年3月14日 08:30 GMT+8*  
*数据来源：ClawHub市场、OpenClaw社区、各大技术博客及券商研报*
