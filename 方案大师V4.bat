@echo off
chcp 65001 >nul
title 施工方案编制大师 V4.0
echo.
echo ===============================================================
echo        施工方案编制大师 V4.0 - 北车上盖学校项目
echo ===============================================================
echo.

set PYTHON=C:\Users\18771\scoop\apps\python\current\python.exe
set SCRIPT=C:\Users\18771\.openclaw\skills\construction-plan-enhanced\construction_plan_master.py

REM 检查参数
if "%~1"=="--single" goto single
if "%~1"=="--phase" goto phase
if "%~1"=="--all" goto all
if "%~1"=="--list" goto list

REM 无参数，进入交互模式
goto interactive

:single
echo [模式] 单方案生成
"%PYTHON%" "%SCRIPT%" --mode single %*
goto end

:phase
echo [模式] 按阶段生成
"%PYTHON%" "%SCRIPT%" --mode phase %*
goto end

:all
echo [模式] 生成所有阶段
echo [提示] 这将生成全部133个方案，请耐心等待...
"%PYTHON%" "%SCRIPT%" --mode all %*
goto end

:list
echo [模式] 查看阶段列表
"%PYTHON%" "%SCRIPT%" --mode list
goto end

:interactive
echo 正在启动交互式菜单...
echo.
"%PYTHON%" "%SCRIPT%"
goto end

:end
echo.
