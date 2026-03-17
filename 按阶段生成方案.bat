@echo off
chcp 65001 >nul
title 北车上盖学校 - 按阶段生成方案 V3.0
echo.
echo ===============================================================
echo    北车上盖学校项目 - 施工方案按阶段生成系统 V3.0
echo ===============================================================
echo.

set PYTHON=C:\Users\18771\scoop\apps\python\current\python.exe
set SCRIPT=C:\Users\18771\.openclaw\skills\construction-plan-enhanced\phase_generator_v3.py

echo 请选择操作:
echo.
echo   [1] 查看所有施工阶段
echo   [2] 生成阶段1 - 施工准备阶段
echo   [3] 生成阶段2 - 桩基及基坑阶段
echo   [4] 生成阶段3 - 基础施工阶段
echo   [5] 生成阶段4 - 主体结构阶段
echo   [6] 生成阶段5 - 装饰装修阶段
echo   [7] 生成阶段6 - 机电安装阶段
echo   [8] 生成阶段7 - 室外工程及收尾阶段
echo   [9] 生成所有阶段
echo   [0] 退出
echo.
set /p CHOICE=请输入选项 [0-9]: 

if "%CHOICE%"=="1" goto list
if "%CHOICE%"=="2" goto phase1
if "%CHOICE%"=="3" goto phase2
if "%CHOICE%"=="4" goto phase3
if "%CHOICE%"=="5" goto phase4
if "%CHOICE%"=="6" goto phase5
if "%CHOICE%"=="7" goto phase6
if "%CHOICE%"=="8" goto phase7
if "%CHOICE%"=="9" goto all
if "%CHOICE%"=="0" goto exit
goto end

:list
cls
echo.
"%PYTHON%" "%SCRIPT%" --list
echo.
pause
goto end

:phase1
cls
echo.
"%PYTHON%" "%SCRIPT%" --phase 1
echo.
echo [完成] 阶段1方案已生成！
echo.
pause
start "" "C:\Users\18771\Documents\施工方案\北车上盖学校\阶段1_施工准备"
goto end

:phase2
cls
echo.
"%PYTHON%" "%SCRIPT%" --phase 2
echo.
echo [完成] 阶段2方案已生成！
echo.
pause
start "" "C:\Users\18771\Documents\施工方案\北车上盖学校\阶段2_桩基基坑"
goto end

:phase3
cls
echo.
"%PYTHON%" "%SCRIPT%" --phase 3
echo.
echo [完成] 阶段3方案已生成！
echo.
pause
start "" "C:\Users\18771\Documents\施工方案\北车上盖学校\阶段3_基础施工"
goto end

:phase4
cls
echo.
"%PYTHON%" "%SCRIPT%" --phase 4
echo.
echo [完成] 阶段4方案已生成！
echo.
pause
start "" "C:\Users\18771\Documents\施工方案\北车上盖学校\阶段4_主体结构"
goto end

:phase5
cls
echo.
"%PYTHON%" "%SCRIPT%" --phase 5
echo.
echo [完成] 阶段5方案已生成！
echo.
pause
start "" "C:\Users\18771\Documents\施工方案\北车上盖学校\阶段5_装饰装修"
goto end

:phase6
cls
echo.
"%PYTHON%" "%SCRIPT%" --phase 6
echo.
echo [完成] 阶段6方案已生成！
echo.
pause
start "" "C:\Users\18771\Documents\施工方案\北车上盖学校\阶段6_机电安装"
goto end

:phase7
cls
echo.
"%PYTHON%" "%SCRIPT%" --phase 7
echo.
echo [完成] 阶段7方案已生成！
echo.
pause
start "" "C:\Users\18771\Documents\施工方案\北车上盖学校\阶段7_室外及收尾"
goto end

:all
cls
echo.
echo [提示] 生成所有阶段需要较长时间，请耐心等待...
echo.
"%PYTHON%" "%SCRIPT%" --all
echo.
echo [完成] 所有阶段方案已生成！
echo.
pause
start "" "C:\Users\18771\Documents\施工方案\北车上盖学校"
goto end

:exit
echo.
echo 感谢使用，再见！
echo.

:end
