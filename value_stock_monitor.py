#!/usr/bin/env python3
"""
低估值稳健股票监控池
目标：招商银行、中国神华、长江电力、格力电器
"""

import requests
import json
from datetime import datetime

# 监控配置
WATCHLIST = [
    {
        "code": "600036",
        "name": "招商银行",
        "market": "sh",
        "target_buy": 37.0,      # 买入目标价
        "target_sell": 50.0,     # 止盈观察价
        "alert_change": 3.0      # 日内异动±3%
    },
    {
        "code": "601088",
        "name": "中国神华",
        "market": "sh",
        "target_buy": 40.0,
        "target_sell": 50.0,
        "alert_change": 3.0
    },
    {
        "code": "600900",
        "name": "长江电力",
        "market": "sh",
        "target_buy": 27.0,
        "target_sell": 32.0,
        "alert_change": 2.5
    },
    {
        "code": "000651",
        "name": "格力电器",
        "market": "sz",
        "target_buy": 38.0,
        "target_sell": 48.0,
        "alert_change": 3.0
    }
]

class ValueStockMonitor:
    """低估值股票监控器"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
    
    def fetch_price(self, code, market):
        """获取实时股价"""
        try:
            url = f"https://hq.sinajs.cn/list={market}{code}"
            resp = self.session.get(url, headers={'Referer': 'https://finance.sina.com.cn'}, timeout=10)
            resp.encoding = 'gb18030'
            
            data_str = resp.text.split('"')[1]
            if not data_str:
                return None
                
            p = data_str.split(',')
            if len(p) > 30 and float(p[3]) > 0:
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
            print(f"获取{code}失败: {e}")
        return None
    
    def check_alerts(self, stock, data):
        """检查预警条件"""
        alerts = []
        price = data['price']
        change_pct = data['change_pct']
        
        # 1. 买入机会（跌到目标价）
        if price <= stock['target_buy']:
            alerts.append({
                'level': 'critical',
                'icon': '🎯',
                'title': '买入机会',
                'msg': f"股价 {price:.2f} 元，低于目标买入价 {stock['target_buy']:.2f} 元"
            })
        
        # 2. 止盈观察（涨过目标价）
        elif price >= stock['target_sell']:
            alerts.append({
                'level': 'info',
                'icon': '💰',
                'title': '止盈观察',
                'msg': f"股价 {price:.2f} 元，超过目标价 {stock['target_sell']:.2f} 元"
            })
        
        # 3. 日内大跌
        if change_pct <= -stock['alert_change']:
            alerts.append({
                'level': 'warning',
                'icon': '📉',
                'title': '日内大跌',
                'msg': f"跌幅 {change_pct:.2f}%"
            })
        
        # 4. 日内大涨
        elif change_pct >= stock['alert_change']:
            alerts.append({
                'level': 'info',
                'icon': '📈',
                'title': '日内大涨',
                'msg': f"涨幅 {change_pct:.2f}%"
            })
        
        return alerts
    
    def format_status(self, stock, data):
        """格式化状态消息"""
        price = data['price']
        change_pct = data['change_pct']
        target = stock['target_buy']
        
        # 计算距离目标价
        distance = ((target - price) / price * 100) if price > target else 0
        
        # 涨跌颜色
        color = "🔴" if change_pct > 0 else "🟢" if change_pct < 0 else "⚪"
        
        # 目标状态
        if price <= target:
            status = "🎯 已触发买入区间！"
        else:
            status = f"📊 还需下跌 {distance:.1f}%"
        
        msg = f"""{color} <b>{stock['name']} ({stock['code']})</b>
💰 现价: <b>{price:.2f} 元</b> ({change_pct:+.2f}%)
🎯 买入目标: {target:.2f} 元 | {status}
📈 最高: {data['high']:.2f} | 最低: {data['low']:.2f}
💹 成交: {data['volume']/10000:.0f}万手
⏰ {data['time']}"""
        
        return msg
    
    def format_alert(self, stock, data, alert):
        """格式化预警消息"""
        change_pct = data['change_pct']
        color = "🔴" if change_pct > 0 else "🟢"
        
        msg = f"""━━━━━━━━━━━━━━━━━━━━
{alert['icon']} <b>{stock['name']} ({stock['code']}) {alert['title']}</b>
━━━━━━━━━━━━━━━━━━━━

{color} 当前价格: <b>{data['price']:.2f} 元</b> ({change_pct:+.2f}%)
📊 涨跌额: {(data['price'] - data['prev_close']):.2f} 元
🎯 买入目标: {stock['target_buy']:.2f} 元
💰 止盈观察: {stock['target_sell']:.2f} 元

<b>{alert['title']}</b>
{alert['msg']}

━━━━━━━━━━━━━━━━━━━━
<i>监控时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}</i>"""
        
        return msg
    
    def run(self, check_alerts=True):
        """运行监控"""
        results = []
        triggered = []
        
        for stock in WATCHLIST:
            data = self.fetch_price(stock['code'], stock['market'])
            if not data:
                continue
            
            # 生成状态报告
            status = self.format_status(stock, data)
            results.append(status)
            
            # 检查预警
            if check_alerts:
                alerts = self.check_alerts(stock, data)
                for alert in alerts:
                    alert_msg = self.format_alert(stock, data, alert)
                    triggered.append(alert_msg)
        
        return results, triggered
    
    def get_summary(self):
        """获取汇总报告"""
        results, triggered = self.run(check_alerts=True)
        
        summary = "📊 <b>低估值股票池监控报告</b>\n"
        summary += "━━━━━━━━━━━━━━━━━━━━\n\n"
        
        for r in results:
            summary += r + "\n\n"
        
        summary += "━━━━━━━━━━━━━━━━━━━━\n"
        summary += "<i>监控规则: 跌到目标价提醒买入，涨跌幅超阈值提醒异动</i>"
        
        return summary, triggered

if __name__ == '__main__':
    monitor = ValueStockMonitor()
    summary, alerts = monitor.get_summary()
    print(summary)
    
    if alerts:
        print("\n\n🚨 触发预警:\n")
        for a in alerts:
            print(a)
            print()
