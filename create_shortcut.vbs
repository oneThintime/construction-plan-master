Set WshShell = WScript.CreateObject("WScript.Shell")
Set oLink = WshShell.CreateShortcut(WshShell.SpecialFolders("Desktop") & "\施工方案编制大师.lnk")
oLink.TargetPath = "C:\Users\18771\.openclaw\skills\construction-plan-enhanced\方案大师V4.bat"
oLink.WorkingDirectory = "C:\Users\18771\.openclaw\skills\construction-plan-enhanced"
oLink.Description = "施工方案编制大师 V4.0 - 北车上盖学校项目"
oLink.IconLocation = "shell32.dll, 21"
oLink.Save
WScript.Echo "桌面快捷方式已创建成功！"
