@echo off
chcp 65001 >nul
title 施工方案编制大师 - 创建桌面快捷方式
echo.
echo ===============================================================
echo        施工方案编制大师 V4.0 - 创建桌面快捷方式
echo ===============================================================
echo.

set DESKTOP=%USERPROFILE%\Desktop
set TARGET=C:\Users\18771\.openclaw\skills\construction-plan-enhanced\方案大师V4.bat
set ICON=C:\Users\18771\.openclaw\skills\construction-plan-enhanced\icon.ico
set WORKDIR=C:\Users\18771\.openclaw\skills\construction-plan-enhanced

echo [信息] 正在创建桌面快捷方式...
echo [信息] 目标: %TARGET%
echo [信息] 桌面: %DESKTOP%
echo.

REM 创建VBScript来生成快捷方式
(
echo Set WshShell = WScript.CreateObject("WScript.Shell"^)
echo Set oLink = WshShell.CreateShortcut(WshShell.SpecialFolders("Desktop"^) ^& "\施工方案编制大师.lnk"^)
echo oLink.TargetPath = "%TARGET%"
echo oLink.WorkingDirectory = "%WORKDIR%"
echo oLink.Description = "施工方案编制大师 V4.0 - 北车上盖学校项目"
echo oLink.IconLocation = "shell32.dll, 21"
echo oLink.Save
) > "%TEMP%\CreateShortcut.vbs"

REM 执行VBScript
cscript //nologo "%TEMP%\CreateShortcut.vbs"

REM 清理临时文件
del "%TEMP%\CreateShortcut.vbs"

if exist "%DESKTOP%\施工方案编制大师.lnk" (
    echo [成功] 桌面快捷方式已创建！
    echo [路径] %DESKTOP%\施工方案编制大师.lnk
    echo.
    echo 提示：双击桌面图标即可启动系统
) else (
    echo [错误] 快捷方式创建失败
    echo.
    echo 尝试创建替代方案...
    goto create_bat
)

goto end

:create_bat
echo [备选] 创建桌面批处理文件...
(
echo @echo off
echo chcp 65001 ^>nul
echo cd /d "C:\Users\18771\.openclaw\skills\construction-plan-enhanced"
echo call 方案大师V4.bat
) > "%DESKTOP%\施工方案大师.bat"

if exist "%DESKTOP%\施工方案大师.bat" (
    echo [成功] 桌面批处理文件已创建！
    echo [路径] %DESKTOP%\施工方案大师.bat
)

:end
echo.
pause
