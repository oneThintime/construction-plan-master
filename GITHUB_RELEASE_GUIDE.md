# GitHub 发布指南

施工方案编制大师 (Construction Plan Master) - GitHub 发布步骤

---

## 📦 发布前准备

### 1. 创建 GitHub 账号
- 访问 https://github.com
- 注册账号并完成验证

### 2. 创建新仓库

```bash
# 在 GitHub 网页上操作
1. 点击右上角 "+" 号
2. 选择 "New repository"
3. 填写仓库信息：
   - Repository name: construction-plan-master
   - Description: 施工方案编制大师 - A comprehensive construction engineering plan generation system
   - Visibility: Public (推荐开源)
   - 勾选 "Add a README file" (我们会替换它)
   - 勾选 "Add .gitignore" 选择 Python
   - 勾选 "Choose a license" 选择 MIT License
4. 点击 "Create repository"
```

### 3. 本地准备

在你的电脑上操作：

```bash
# 进入项目目录
cd C:\Users\18771\.openclaw\skills\construction-plan-enhanced

# 初始化 Git 仓库
git init

# 添加远程仓库（用你的用户名替换 yourusername）
git remote add origin https://github.com/yourusername/construction-plan-master.git

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Construction Plan Master v4.0"

# 推送到 GitHub
git branch -M main
git push -u origin main
```

---

## 🚀 发布步骤

### Step 1: 确保文件完整

检查以下文件是否齐全：

```
construction-plan-master/
├── README.md                      ✅ 主说明文件（双语）
├── LICENSE                        ✅ MIT 许可证
├── .gitignore                     ✅ Git 忽略文件
├── CONTRIBUTING.md                ✅ 贡献指南
├── CHANGELOG.md                   ✅ 更新日志
├── requirements.txt               ✅ 依赖列表
├── construction_plan_master.py    ✅ 主程序
├── complete_plan_generator.py     ✅ 完整方案生成器
├── phase_generator_v3.py          ✅ V3.0 阶段生成器
├── plan_generator_v2.py           ✅ V2.0 多模板生成器
├── construction_plan_enhanced.py  ✅ V1.0 基础生成器
├── templates/                     ✅ 模板目录
│   ├── phase_configs.py
│   ├── plan_configs.py
│   ├── calculations.py
│   └── __init__.py
├── generators/                    ✅ 生成器目录
│   ├── ai_content.py
│   ├── xlsx_generator.py
│   └── __init__.py
├── docs/                          ✅ 文档目录
│   └── (screenshots, guides)
└── [启动脚本]                      ✅ Windows 批处理文件
```

### Step 2: 创建 Release

在 GitHub 网页上：

```
1. 进入仓库主页
2. 点击右侧 "Releases"
3. 点击 "Create a new release"
4. 填写发布信息：
   - Choose a tag: v4.0.0
   - Release title: Construction Plan Master v4.0.0
   - Describe this release:

## What's New in v4.0.0

### 🌟 主要功能
- 单方案生成模式：生成单个危大工程完整方案
- 阶段批量生成：按7个施工阶段生成全部133个方案
- 交互式菜单：用户友好的命令行界面
- 完整方案内容：超过8000字的详细方案

### 📊 项目示例
- 北车上盖学校新建工程
- 133个完整施工方案
- 14个需专家论证方案
- 94个紧急方案

### 🛠️ 技术特点
- Excel计算书自动生成
- AI提示词生成
- 专家论证自动识别
- 桌面快捷方式一键创建

### 📁 文件说明
- construction_plan_master.py: 主程序 V4.0
- complete_plan_generator.py: 完整方案生成器
- 方案大师V4.bat: Windows启动脚本

### 📖 使用文档
详见 README.md

---

## Installation

```bash
pip install -r requirements.txt
python construction_plan_master.py
```

## Quick Start

Double-click `方案大师V4.bat` or run:
```bash
python construction_plan_master.py --mode list
```

5. 点击 "Publish release"
```

### Step 3: 添加 Topics（标签）

在仓库主页：
```
1. 点击右侧 "About" 旁边的齿轮图标
2. 在 Topics 中添加：
   - construction
   - civil-engineering
   - python
   - automation
   - chinese
   - deep-excavation
   - safety
   - engineering-tools
   - building-codes
   - openclaw
3. 保存
```

### Step 4: 启用 GitHub Pages（可选）

创建项目文档网站：

```
1. 进入 Settings
2. 左侧选择 Pages
3. Source 选择 Deploy from a branch
4. Branch 选择 main，folder 选择 /docs
5. 点击 Save
```

---

## 📸 截图准备

建议在 README 中添加以下截图：

1. **主界面截图**：显示交互式菜单
2. **生成的方案示例**：显示完整方案内容
3. **目录结构**：显示生成的文件组织
4. **Excel计算书**：显示土压力计算表
5. **项目示例**：北车上盖学校项目清单

截图保存到 `docs/screenshots/` 目录

---

## 📝 README 优化建议

在 README.md 中添加以下内容（可选）：

### 1.  badges（徽章）
```markdown
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://microsoft.com/windows)
```

### 2. Logo
如果有项目 Logo，可以放在 README 顶部

### 3. Screenshots
```markdown
## 📸 Screenshots

![Main Menu](docs/screenshots/main-menu.png)
*Main Menu Interface*

![Generated Plan](docs/screenshots/generated-plan.png)
*Sample Generated Plan*
```

---

## 🔄 后续维护

### 更新版本

```bash
# 修改版本号后
git add .
git commit -m "Release v4.0.1 - Bug fixes"
git push

# 在 GitHub 创建新 Release
tag: v4.0.1
title: v4.0.1 Bug Fixes
```

### 回应 Issues

定期检查并回应：
- Bug 报告
- 功能请求
- 使用问题

### 合并 Pull Requests

1. 审查代码
2. 测试功能
3. 合并到 main 分支
4. 更新 CHANGELOG.md

---

## 🌟 推广建议

### 1. 分享链接
- 微信朋友圈
- 技术论坛（知乎、掘金、CSDN）
- 工程行业群

### 2. 写文章
撰写介绍文章：
- 《如何用Python自动生成施工方案》
- 《施工方案编制大师使用指南》
- 《北车上盖学校133个方案自动生成实践》

### 3. 投稿
- 投稿到 Python 中文社区
- 投稿到工程行业公众号
- 参加开源项目比赛

---

## 📞 联系方式模板

在 README 中添加：

```markdown
## 👤 Author

**大虾 (Da Xia)**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your-email@example.com
- Project: [Construction Plan Master](https://github.com/yourusername/construction-plan-master)

## 🤝 Contributing

欢迎贡献代码！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

## 📜 License

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件
```

---

## ✅ 发布检查清单

- [ ] GitHub 仓库已创建
- [ ] 所有代码已推送到 main 分支
- [ ] README.md 完整（双语）
- [ ] LICENSE 文件已添加
- [ ] CHANGELOG.md 已更新
- [ ] CONTRIBUTING.md 已添加
- [ ] .gitignore 已配置
- [ ] Release v4.0.0 已发布
- [ ] Topics 标签已添加
- [ ] 截图已添加到 docs/

---

**祝发布成功！** 🎉

如有问题，随时联系我！
