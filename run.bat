@echo off
chcp 65001 >nul
echo.
echo 🚀 增强版施工方案编制系统
echo ========================
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️  未检测到 Python，请先安装 Python 3.8+
    echo    下载地址: https://python.org/downloads
    echo.
    echo 或者使用 Node.js 运行: node run.js
    pause
    exit /b 1
)

REM 运行程序
cd /d "%~dp0"
python construction_plan_enhanced.py %*

pause
