@echo off
chcp 65001 >nul
title 施工方案编制系统 V2.0
echo.
echo =====================================
echo    增强版施工方案编制系统 V2.0
echo    [支持多种方案模板]
echo =====================================
echo.

REM 使用 Scoop Python
set PYTHON=C:\Users\18771\scoop\apps\python\current\python.exe
set SCRIPT=C:\Users\18771\.openclaw\skills\construction-plan-enhanced\plan_generator_v2.py

REM 显示可用方案类型
echo [可用方案类型]
echo   1. 深基坑 (默认)
echo   2. 高支模
echo   3. 脚手架
echo   4. 塔吊基础
echo   5. 施工用电
echo   6. 起重吊装
echo.

REM 交互输入
echo 请输入工程信息（直接回车使用默认值）:
echo.
set /p NAME=工程名称 [新建工程]: 
if "!NAME!"=="" set NAME=新建工程

set /p TYPE_INPUT=方案类型编号 [1]: 
if "!TYPE_INPUT!"=="" set TYPE_INPUT=1

REM 转换编号为类型名称
if %TYPE_INPUT%==1 set TYPE=深基坑
if %TYPE_INPUT%==2 set TYPE=高支模
if %TYPE_INPUT%==3 set TYPE=脚手架
if %TYPE_INPUT%==4 set TYPE=塔吊基础
if %TYPE_INPUT%==5 set TYPE=施工用电
if %TYPE_INPUT%==6 set TYPE=起重吊装

REM 根据类型询问特定参数
if "%TYPE%"=="深基坑" (
    set /p DEPTH=基坑深度 [12]: 
    if "!DEPTH!"=="" set DEPTH=12
    set EXTRA_PARAM=--depth !DEPTH!
)

if "%TYPE%"=="高支模" (
    set /p HEIGHT=搭设高度 [8]: 
    if "!HEIGHT!"=="" set HEIGHT=8
    set EXTRA_PARAM=--height !HEIGHT!
)

if "%TYPE%"=="脚手架" (
    set /p HEIGHT=搭设高度 [50]: 
    if "!HEIGHT!"=="" set HEIGHT=50
    set EXTRA_PARAM=--height !HEIGHT!
)

if "%TYPE%"=="塔吊基础" (
    set /p MODEL=塔吊型号 [TC5613]: 
    if "!MODEL!"=="" set MODEL=TC5613
    set EXTRA_PARAM=--tower-model !MODEL!
)

if "%TYPE%"=="起重吊装" (
    set /p WEIGHT=构件重量 [100]: 
    if "!WEIGHT!"=="" set WEIGHT=100
    set EXTRA_PARAM=--weight !WEIGHT!
)

echo.
echo [开始] 正在生成 %TYPE% 施工方案...
echo.

"%PYTHON%" "%SCRIPT%" --name "%NAME%" --type "%TYPE%" %EXTRA_PARAM%

echo.
echo 按任意键打开输出目录...
pause >nul

start "" "C:\Users\18771\Documents\施工方案"
