# Python 环境配置脚本
# 保存为: setup_python.ps1
# 运行方式: 右键选择"使用 PowerShell 运行"

Write-Host "🚀 正在配置 Python 环境..." -ForegroundColor Green
Write-Host "==========================" 

# 检查 scoop 是否安装
if (!(Get-Command scoop -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️  未检测到 Scoop，正在安装..." -ForegroundColor Yellow
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
}

# 检查 Python 是否已安装
$pythonInstalled = scoop list python 2>$null | Select-String "python"

if ($pythonInstalled) {
    Write-Host "✅ Python 已安装，跳过安装步骤" -ForegroundColor Green
} else {
    Write-Host "📦 正在通过 Scoop 安装 Python..." -ForegroundColor Cyan
    scoop install python
}

# 刷新环境变量
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","User") + ";" + [System.Environment]::GetEnvironmentVariable("Path","Machine")

# 验证安装
Write-Host ""
Write-Host "🔍 验证 Python 安装..." -ForegroundColor Cyan
python --version

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Python 安装成功!" -ForegroundColor Green
    
    # 安装依赖
    Write-Host ""
    Write-Host "📦 正在安装 openpyxl..." -ForegroundColor Cyan
    pip install openpyxl -q
    
    Write-Host "📦 正在安装 python-docx..." -ForegroundColor Cyan
    pip install python-docx -q
    
    Write-Host ""
    Write-Host "✅ 所有依赖安装完成!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🎉 现在可以运行施工方案编制系统了:" -ForegroundColor Yellow
    Write-Host "   cd C:\Users\18771\.openclaw\skills\construction-plan-enhanced"
    Write-Host "   python construction_plan_enhanced.py --name '测试项目' --depth 12"
} else {
    Write-Host "❌ Python 安装失败，请检查错误信息" -ForegroundColor Red
}

Write-Host ""
Write-Host "按任意键退出..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
