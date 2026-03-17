@echo off
chcp 65001 >nul
title 施工方案编制系统
echo.
echo =====================================
echo    增强版施工方案编制系统
echo =====================================
echo.

REM 使用 Scoop Python
set PYTHON=C:\Users\18771\scoop\apps\python\current\python.exe
set SCRIPT=C:\Users\18771\.openclaw\skills\construction-plan-enhanced\construction_plan_enhanced.py

REM 默认参数
set NAME=新建工程
set TYPE=深基坑
set DEPTH=10

REM 交互输入
echo 请输入工程信息（直接回车使用默认值）:
echo.
set /p NAME=工程名称 [%NAME%]: 
set /p TYPE=方案类型 [%TYPE%]: 
set /p DEPTH=基坑深度 [%DEPTH%]: 

echo.
echo [开始] 正在生成施工方案...
echo.

"%PYTHON%" "%SCRIPT%" --name "%NAME%" --type "%TYPE%" --depth %DEPTH%

echo.
echo 按任意键打开输出目录...
pause >nul

start "" "C:\Users\18771\Documents\施工方案"
