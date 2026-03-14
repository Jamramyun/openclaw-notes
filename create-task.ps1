# Create scheduled task
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-ExecutionPolicy Bypass -File C:\openclaw\openclaw-notes\check-tasks.ps1'
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(5) -RepetitionInterval (New-TimeSpan -Minutes 30)
Register-ScheduledTask -TaskName 'XiaogongTaskCheck' -Action $action -Trigger $trigger -Force
Write-Host "Done! Scheduled task created."
