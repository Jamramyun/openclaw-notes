$beijingTime = (Get-Date).ToUniversalTime().AddHours(8)
Write-Host "`$(`$beijingTime.ToString('yyyy-MM-dd HH:mm:ss')) [北京时间] - 虾工开始检查任务..." -ForegroundColor Cyan
cd C:\openclaw\openclaw-notes

# 拉取最新代码
git pull origin master:main --force 2>$null

# 检查是否有新的 Issue（简单版本：检查文件标记）
$flagFile = "C:\openclaw\openclaw-notes\NEW_TASK.flag"
if (Test-Path $flagFile) {
    Write-Host "⚠️ 发现新任务标记文件！" -ForegroundColor Yellow
    $taskContent = Get-Content $flagFile -Raw
    Write-Host "任务内容：" -ForegroundColor White
    Write-Host $taskContent
    Write-Host ""
    Write-Host "请龙虾老大确认后，我将执行任务！" -ForegroundColor Green
} else {
    Write-Host "✅ 无新任务" -ForegroundColor Green
}

Write-Host "检查完成，下次检查：30分钟后" -ForegroundColor Gray
