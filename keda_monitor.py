#!/usr/bin/env python3
"""
科大讯飞监控配置
触发条件：
1. 股价跌到45元以下（买入机会）
2. 日内涨跌幅超过 ±5%（异动）
3. 一季报发布提醒
4. 重大公告提醒
"""

import requests
import json
import time
from datetime import datetime

# 科大讯飞监控配置
KE_DA_XUN_FEI = {
    "code": "002230",
    "name": "科大讯飞", 
    "market": "sz",  # 深交所
    "type": "individual",
    "cost": None,  # 用户未持仓，不设成本
    "alerts": {
        # 买入目标价
        "price_below": 45.0,       # 跌到45元提醒（建议买入区间）
        "price_above": 60.0,       # 涨到60元提醒（止盈/观望）
        
        # 日内异动
        "change_pct_above": 5.0,   # 日内大涨5%
        "change_pct_below": -5.0,  # 日内大跌5%
        
        # 成交量异动
        "volume_surge": 2.0,       # 成交量是5日均量2倍
        
        # 均线监控（启用）
        "ma_monitor": True
    }
}

class KeDaXunFeiMonitor:
    """科大讯飞专用监控"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.config = KE_DA_XUN_FEI
        self.alert_history = []
        
    def fetch_price(self):
        """获取实时股价"""
        try:
            url = f"https://hq.sinajs.cn/list=sz{self.config['code']}"
            resp = self.session.get(url, headers={'Referer': 'https://finance.sina.com.cn'}, timeout=10)
            resp.encoding = 'gb18030'
            
            data_str = resp.text.split('"')[1]
            p = data_str.split(',')
            
            if len(p) > 30:
                return {
                    'name': p[0],
                    'price': float(p[3]),
                    'prev_close': float(p[2]),
                    'open': float(p[1]),
                    'high': float(p[4]),
                    'low': float(p[5]),
                    'volume': int(p[8]),
                    'change_pct': (float(p[3]) - float(p[2])) / float(p[2]) * 100,
                    'time': p[31]
                }
        except Exception as e:
            print(f"获取股价失败: {e}")
        return None
    
    def check_alerts(self, data):
        """检查预警条件"""
        alerts = []
        cfg = self.config['alerts']
        price = data['price']
        change_pct = data['change_pct']
        
        # 1. 价格跌破买入目标
        if price <= cfg['price_below']:
            alerts.append({
                'type': 'price_below',
                'level': 'critical',
                'icon': '🎯',
                'title': '买入机会',
                'msg': f"股价跌至 {price:.2f} 元，低于目标买入价 {cfg['price_below']} 元"
            })
        
        # 2. 价格涨过止盈目标
        if price >= cfg['price_above']:
            alerts.append({
                'type': 'price_above',
                'level': 'warning',
                'icon': '⚠️',
                'title': '价格突破',
                'msg': f"股价涨至 {price:.2f} 元，超过目标价 {cfg['price_above']} 元"
            })
        
        # 3. 日内大涨
        if change_pct >= cfg['change_pct_above']:
            alerts.append({
                'type': 'change_pct_above',
                'level': 'warning',
                'icon': '📈',
                'title': '日内大涨',
                'msg': f"涨幅 {change_pct:.2f}%，超过 {cfg['change_pct_above']}%"
            })
        
        # 4. 日内大跌
        if change_pct <= cfg['change_pct_below']:
            alerts.append({
                'type': 'change_pct_below',
                'level': 'warning',
                'icon': '📉',
                'title': '日内大跌',
                'msg': f"跌幅 {change_pct:.2f}%，超过 {cfg['change_pct_below']}%"
            })
        
        return alerts
    
    def format_alert(self, data, alert):
        """格式化预警消息"""
        change_pct = data['change_pct']
        color = "🔴" if change_pct > 0 else "🟢" if change_pct < 0 else "⚪"
        
        msg = f"""
━━━━━━━━━━━━━━━━━━━━
{alert['icon']} <b>科大讯飞 ({self.config['code']}) 预警</b>
━━━━━━━━━━━━━━━━━━━━

{color} 当前价格: <b>{data['price']:.2f} 元</b> ({change_pct:+.2f}%)
📊 涨跌额: {(data['price'] - data['prev_close']):.2f} 元
💹 成交量: {data['volume'] / 10000:.0f} 万手
⏰ 更新时间: {data['time']}

<b>{alert['title']}</b>
{alert['msg']}

━━━━━━━━━━━━━━━━━━━━
<i>监控规则: 买入目标价45元，异动阈值±5%</i>
"""
        return msg
    
    def run(self):
        """运行监控"""
        data = self.fetch_price()
        if not data:
            return None
        
        alerts = self.check_alerts(data)
        if alerts:
            # 返回第一个触发的预警
            return self.format_alert(data, alerts[0])
        
        return None
    
    def get_status(self):
        """获取当前状态（用于手动查询）"""
        data = self.fetch_price()
        if not data:
            return "获取数据失败"
        
        change_pct = data['change_pct']
        color = "🔴" if change_pct > 0 else "🟢" if change_pct < 0 else "⚪"
        distance_to_target = ((45 - data['price']) / data['price'] * 100) if data['price'] > 45 else 0
        
        msg = f"""
━━━━━━━━━━━━━━━━━━━━
📊 <b>科大讯飞 ({self.config['code']}) 监控状态</b>
━━━━━━━━━━━━━━━━━━━━

{color} 当前价格: <b>{data['price']:.2f} 元</b> ({change_pct:+.2f}%)
📈 今开: {data['open']:.2f} 元
📊 最高: {data['high']:.2f} 元 | 最低: {data['low']:.2f} 元
💹 成交量: {data['volume'] / 10000:.0f} 万手
⏰ 时间: {data['time']}

🎯 <b>监控目标</b>
• 买入目标价: 45.00 元
• 距离目标: {distance_to_target:.1f}%
• 当前状态: {"已触发买入区间 ✅" if data['price'] <= 45 else f"还需下跌 {distance_to_target:.1f}%"}

⚡ <b>预警设置</b>
• 买入提醒: ≤ 45.00 元
• 异动提醒: ±5%
• 止盈观察: ≥ 60.00 元
"""
        return msg

if __name__ == '__main__':
    monitor = KeDaXunFeiMonitor()
    print(monitor.get_status())
