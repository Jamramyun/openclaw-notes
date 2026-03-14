#!/bin/bash
# 配置 Tavily API Key

echo "🔄 配置 Tavily API Key..."

# 写入环境变量文件
echo "export TAVILY_API_KEY=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" >> ~/.bashrc
echo "export TAVILY_API_KEY=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" >> ~/.profile

# 当前会话生效
export TAVILY_API_KEY=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

echo "✅ API Key 配置完成！"
echo ""
echo "测试搜索功能..."
