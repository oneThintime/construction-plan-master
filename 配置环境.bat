@echo off
chcp 65001 >nul
title 施工方案系统 - Python环境配置
echo.
echo ===========================================
echo   施工方案编制系统 - Python环境配置工具
echo ===========================================
echo.

REM 检查 PowerShell
powershell -Command "Get-Host" >nul 2>&1
if errorlevel 1 (
    echo ❌ 无法运行 PowerShell，请手动安装 Python
    echo    下载地址: https://python.org/downloads
    pause
    exit /b 1
)

echo 🔧 正在运行 PowerShell 配置脚本...
echo.

REM 运行 PowerShell 脚本
powershell -ExecutionPolicy Bypass -File "%~dp0setup_python.ps1"

echo.
echo 配置完成!
pause
