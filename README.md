# Construction Plan Master (施工方案编制大师)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://microsoft.com/windows)

> A comprehensive construction engineering plan generation system for civil engineering projects, specifically designed for Chinese building codes and standards.

[中文说明](#中文说明) | [English](#english)

---

## 🌟 Features

### Version 4.0 (Latest)
- **Single Plan Mode**: Generate detailed construction plans for individual hazardous projects with calculation sheets
- **Phase-based Batch Mode**: Generate all 133 plans organized by 7 construction phases
- **Expert Review Reminders**: Automatic identification of plans requiring expert review
- **AI Prompts**: Generate AI prompts for detailed content creation

### Supported Plan Types
- Deep Excavation (深基坑)
- High Formwork Support (高支模)
- Scaffolding (脚手架)
- Tower Crane Foundation (塔吊基础)
- Temporary Electricity (施工用电)
- Lifting Operations (起重吊装)

### Project Example: BeiChe ShangGai School
A complete set of 133 construction plans for the "BeiChe ShangGai School New Construction Project":
- Phase 1: Construction Preparation (17 plans)
- Phase 2: Pile Foundation & Excavation (14 plans)
- Phase 3: Foundation Construction (14 plans)
- Phase 4: Main Structure (32 plans)
- Phase 5: Decoration & Finishing (17 plans)
- Phase 6: M&E Installation (16 plans)
- Phase 7: External Works & Handover (23 plans)

---

## 🚀 Quick Start

### Prerequisites
- Windows 10/11
- Python 3.8 or higher
- Microsoft Excel (for calculation sheets)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/construction-plan-master.git

# Navigate to directory
cd construction-plan-master

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### Method 1: Interactive Menu (Recommended)
```bash
# Double-click the desktop shortcut or run:
方案大师V4.bat
```

#### Method 2: Command Line
```bash
# Single plan generation
python construction_plan_master.py --mode single --name "Project Name" --type "Deep Excavation" --depth 12

# List all construction phases
python construction_plan_master.py --mode list

# Generate specific phase (1-7)
python construction_plan_master.py --mode phase --phase 1

# Generate all 133 plans
python construction_plan_master.py --mode all --name "Project Name"
```

---

## 📁 Project Structure

```
construction-plan-master/
├── construction_plan_master.py    # Main program (V4.0)
├── complete_plan_generator.py     # Complete plan generator
├── phase_generator_v3.py          # Phase-based generator (V3.0)
├── plan_generator_v2.py           # Multi-template generator (V2.0)
├── construction_plan_enhanced.py  # Basic generator (V1.0)
├── templates/
│   ├── phase_configs.py           # Phase configurations (133 plans)
│   ├── plan_configs.py            # Plan type templates
│   ├── calculations.py            # Calculation sheet generators
│   └── __init__.py
├── generators/
│   ├── ai_content.py              # AI prompt generator
│   ├── xlsx_generator.py          # Excel generator
│   └── __init__.py
├── 方案大师V4.bat                 # Windows launcher
├── requirements.txt               # Dependencies
├── README.md                      # This file
├── LICENSE                        # MIT License
└── docs/                          # Documentation
```

---

## 📊 Output Files

### Single Plan Mode
- `{Project}_{Type}_方案.txt` - Plan outline
- `{Project}_{Type}_计算书.xlsx` - Calculation sheets
- `{Project}_{Type}_AI提示.txt` - AI prompts

### Phase Mode
```
Project_Directory/
├── Phase1_Construction_Preparation/
│   ├── 01_策划类_施工组织设计.txt
│   ├── 02_策划类_质量策划书.txt
│   └── _阶段方案汇总.txt
├── Phase2_Pile_Foundation/
├── ...
└── _项目方案总清单.txt
```

---

## 🏗️ Construction Phases

| Phase | Name | Plans | Urgent | Expert Review |
|-------|------|-------|--------|---------------|
| 1 | Construction Preparation | 17 | 13 | 0 |
| 2 | Pile Foundation & Excavation | 14 | 10 | 2 |
| 3 | Foundation Construction | 14 | 11 | 3 |
| 4 | Main Structure | 32 | 23 | 5 |
| 5 | Decoration & Finishing | 17 | 16 | 3 |
| 6 | M&E Installation | 16 | 9 | 1 |
| 7 | External Works | 23 | 12 | 0 |
| **Total** | | **133** | **94** | **14** |

---

## 🎯 Plan Categories

| Level | Type | Count | Description |
|-------|------|-------|-------------|
| A | Major Hazardous | 1 | Requires expert review |
| B | Hazardous | 29 | Special construction plan required |
| C | General Safety | 6 | Safety management plan |
| D | Regular | 80 | Project department approval |

---

## 🛠️ Configuration

### Adding New Plan Types

Edit `templates/plan_configs.py`:

```python
PLAN_TEMPLATES = {
    "New Type": {
        "description": "Description of the plan type",
        "expert_threshold": {"param": "depth", "value": 5, "unit": "m"},
        "codes": ["Code 1", "Code 2"],
        "hazards": ["Hazard 1", "Hazard 2"],
        "calculations": ["calc_type_1"],
        "required_params": ["param1", "param2"],
        "ai_sections": ["Section 1", "Section 2"]
    }
}
```

### Adding New Construction Phases

Edit `templates/phase_configs.py`:

```python
"Phase8_New_Phase": {
    "phase_name": "New Phase",
    "time_range": "Month X-Y",
    "description": "Phase description",
    "plans": [
        {"name": "Plan Name", "type": "Category", "level": "B", "urgent": True}
    ]
}
```

---

## 📖 Documentation

- [How to Add New Templates](如何添加新模板.md) (Chinese)
- [Desktop Shortcut Guide](桌面快捷方式说明.txt) (Chinese)
- [Skill Documentation](SKILL.md) (Chinese)

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Ways to Contribute
1. Report bugs and request features via [Issues](../../issues)
2. Submit improvements via [Pull Requests](../../pulls)
3. Share your project examples
4. Help with documentation translation

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Project data source: BeiChe ShangGai School Construction Plan List (Nov 26, 2025)
- Inspired by: CAD-BIM-to-Code-Automation, bimflowsuite
- Framework: OpenClaw

---

## 📞 Contact

- Author: 大虾 (Da Xia)
- Project: Construction Plan Master
- Email: [your-email@example.com]

---

# 中文说明

## 🌟 功能特点

### V4.0 版本（最新）
- **单方案模式**: 生成单个危大工程详细方案（含计算书）
- **阶段批量模式**: 按7个施工阶段批量生成全部133个方案
- **专家论证提醒**: 自动识别需专家论证的方案
- **AI提示生成**: 为详细内容创作生成AI提示词

### 支持的方案类型
- 深基坑工程
- 高支模工程
- 脚手架工程
- 塔吊基础工程
- 施工临时用电
- 起重吊装作业

### 示例项目：北车上盖学校
完整的133个施工方案：
- 阶段1: 施工准备（17个方案）
- 阶段2: 桩基及基坑（14个方案）
- 阶段3: 基础施工（14个方案）
- 阶段4: 主体结构（32个方案）
- 阶段5: 装饰装修（17个方案）
- 阶段6: 机电安装（16个方案）
- 阶段7: 室外及收尾（23个方案）

---

## 🚀 快速开始

### 系统要求
- Windows 10/11
- Python 3.8+
- Microsoft Excel（用于计算书）

### 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/construction-plan-master.git

# 进入目录
cd construction-plan-master

# 安装依赖
pip install -r requirements.txt
```

### 使用方法

#### 方式1：交互式菜单（推荐）
```bash
# 双击桌面快捷方式或运行:
方案大师V4.bat
```

#### 方式2：命令行
```bash
# 单方案生成
python construction_plan_master.py --mode single --name "工程名称" --type "深基坑" --depth 12

# 查看所有阶段
python construction_plan_master.py --mode list

# 生成指定阶段（1-7）
python construction_plan_master.py --mode phase --phase 1

# 生成全部133个方案
python construction_plan_master.py --mode all --name "工程名称"
```

---

## 📊 输出文件

### 单方案模式
- `{工程名}_{类型}_方案.txt` - 方案大纲
- `{工程名}_{类型}_计算书.xlsx` - Excel计算书
- `{工程名}_{类型}_AI提示.txt` - AI提示词

### 阶段模式
```
项目目录/
├── 阶段1_施工准备/
│   ├── 01_策划类_施工组织设计.txt
│   ├── 02_策划类_质量策划书.txt
│   └── _阶段方案汇总.txt
├── 阶段2_桩基基坑/
├── ...
└── _项目方案总清单.txt
```

---

## 🏗️ 施工阶段

| 阶段 | 名称 | 方案数 | 紧急 | 需论证 |
|------|------|--------|------|--------|
| 1 | 施工准备阶段 | 17 | 13 | 0 |
| 2 | 桩基及基坑阶段 | 14 | 10 | 2 |
| 3 | 基础施工阶段 | 14 | 11 | 3 |
| 4 | 主体结构阶段 | 32 | 23 | 5 |
| 5 | 装饰装修阶段 | 17 | 16 | 3 |
| 6 | 机电安装阶段 | 16 | 9 | 1 |
| 7 | 室外及收尾阶段 | 23 | 12 | 0 |
| **合计** | | **133** | **94** | **14** |

---

## 🎯 方案级别

| 级别 | 类型 | 数量 | 说明 |
|------|------|------|------|
| A类 | 超过一定规模的危大工程 | 1 | 需专家论证 |
| B类 | 危大工程 | 29 | 需编制专项方案 |
| C类 | 一般安全专项 | 6 | 需审批 |
| D类 | 普通施工方案 | 80 | 项目部审批 |

---

## 📜 开源协议

本项目采用 MIT 协议 - 详见 [LICENSE](LICENSE) 文件。

---

**Made with ❤️ by 大虾 (Da Xia)**
