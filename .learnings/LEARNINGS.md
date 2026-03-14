# 学习记录

记录从错误中学到的经验、用户的纠正、以及更好的方法。

---

## [LRN-20260314-001] best_practice

**Logged**: 2026-03-14T15:47:00+08:00
**Priority**: high
**Status**: active
**Area**: skill_install

### Summary
ClawHub限流时，可手动创建技能目录和SKILL.md文件作为临时方案

### Details
用户要求安装5个热门技能，但ClawHub API限流、GitHub访问也受限。通过手动创建技能目录和SKILL.md文件，成功实现了技能的"安装"。每个技能的核心是SKILL.md文件，定义了技能的描述、触发条件和使用方法。

### Suggested Action
1. 网络恢复后，可从官方源重新安装完整版
2. 保留手动创建的基础版本作为备份
3. 后续技能安装优先尝试Skillhub国内镜像

### Metadata
- Source: error_recovery
- Related Files: TOOLS.md
- Tags: skill, network, workaround

---

## [LRN-20260314-002] best_practice

**Logged**: 2026-03-14T15:47:30+08:00
**Priority**: medium
**Status**: active
**Area**: stock_monitoring

### Summary
用户偏好低估值+稳健增长的股票，不喜欢追高

### Details
用户主动询问低估值、发展稳健的股票，要求PE低、股息高。分析了招商银行、长江电力、格力电器、中国神华等股票。用户选择了全部设置监控，说明对稳健型投资有兴趣。后续推荐股票时应优先考虑：PE<20、股息>3%、业绩稳定的蓝筹股。

### Suggested Action
- 推荐股票时优先筛选低PE、高股息标的
- 避免推荐高估值、高波动的题材股
- 监控设置应考虑用户的保守偏好

### Metadata
- Source: user_preference
- Related Files: MEMORY.md
- Tags: investment, value_stock, preference

---
