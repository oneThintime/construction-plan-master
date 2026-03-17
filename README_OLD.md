# 增强版施工方案编制系统 - 快速开始

## 🚀 系统版本

| 版本 | 功能 | 说明 |
|------|------|------|
| V1.0 | construction_plan_enhanced.py | 基础版，单方案生成 |
| V2.0 | plan_generator_v2.py | 多模板版，支持6种方案类型 |
| **V3.0** | **phase_generator_v3.py** | **北车上盖学校专用，按施工阶段批量生成** |

---

## 🎯 V3.0 按施工阶段生成（推荐）

### 专为北车上盖学校项目定制

**项目概况**：松岗街道北车上盖保障房配套九年制学校新建工程

**方案总数**：133个，分为7个施工阶段

### 施工阶段划分

| 阶段 | 名称 | 时间 | 方案数 | 紧急方案 |
|------|------|------|--------|----------|
| 阶段1 | 施工准备阶段 | 开工前1-2个月 | 17个 | 13个 |
| 阶段2 | 桩基及基坑阶段 | 开工后1-3个月 | 14个 | 10个 |
| 阶段3 | 基础施工阶段 | 开工后2-4个月 | 14个 | 11个 |
| 阶段4 | 主体结构阶段 | 开工后4-10个月 | 32个 | 23个 |
| 阶段5 | 装饰装修阶段 | 开工后8-14个月 | 17个 | 16个 |
| 阶段6 | 机电安装阶段 | 开工后10-16个月 | 16个 | 9个 |
| 阶段7 | 室外工程及收尾阶段 | 开工后14-18个月 | 23个 | 12个 |

### 使用方法

**方式 1：交互式菜单（推荐）**
```
双击: 按阶段生成方案.bat
```
然后选择要生成的阶段

**方式 2：命令行**
```bash
cd C:\Users\18771\.openclaw\skills\construction-plan-enhanced

# 查看所有阶段
python phase_generator_v3.py --list

# 生成指定阶段（1-7）
python phase_generator_v3.py --phase 1

# 生成所有阶段
python phase_generator_v3.py --all
```

### 输出结构
```
C:\Users\18771\Documents\施工方案\北车上盖学校\
├── 阶段1_施工准备\
│   ├── 01_策划类_施工组织设计（主体工程）.txt
│   ├── 02_策划类_施工组织设计（桩基、支护、土石方）.txt
│   ├── ...
│   └── _阶段方案汇总.txt
├── 阶段2_桩基基坑\
│   └── ...
├── ...
└── _项目方案总清单.txt
```

---

## 🔧 V2.0 多模板版本

支持6种方案类型：深基坑、高支模、脚手架、塔吊基础、施工用电、起重吊装

```bash
# 快速生成（交互式）
双击: 快速生成V2.bat

# 命令行
python plan_generator_v2.py --name "工程名" --type "深基坑" --depth 12
```

---

## 📝 V1.0 基础版本

单方案生成，适用于简单场景

```bash
python construction_plan_enhanced.py --name "测试项目" --depth 10
```

---

## ⚙️ 环境配置

### 一键配置（推荐）
```
双击运行: 配置环境.bat
```

### 手动配置
```bash
pip install openpyxl python-docx
```

---

## 📊 功能对比

| 功能 | V1.0 | V2.0 | V3.0 |
|------|------|------|------|
| 单方案生成 | ✅ | ✅ | ✅ |
| 多方案类型 | ❌ | ✅ (6种) | ✅ (133个) |
| 按阶段生成 | ❌ | ❌ | ✅ (7阶段) |
| 批量生成 | ❌ | ❌ | ✅ |
| 紧急程度标记 | ❌ | ❌ | ✅ |
| 专家论证提醒 | ❌ | ✅ | ✅ |
| 阶段汇总 | ❌ | ❌ | ✅ |
| 项目总清单 | ❌ | ❌ | ✅ |

---

## 🆘 常见问题

**Q: 提示 'python' 不是内部或外部命令？**  
A: 运行 `配置环境.bat` 或手动安装 Python

**Q: 如何添加新的方案类型？**  
A: 查看 `如何添加新模板.md`

**Q: 方案生成后怎么修改？**  
A: 直接编辑生成的 .txt 文件，或修改 `templates/phase_configs.py` 后重新生成

---

## 📁 文件说明

| 文件 | 用途 |
|------|------|
| `phase_generator_v3.py` | V3.0主程序 - 按阶段生成 |
| `plan_generator_v2.py` | V2.0主程序 - 多模板 |
| `construction_plan_enhanced.py` | V1.0主程序 - 基础版 |
| `按阶段生成方案.bat` | V3.0启动脚本 |
| `快速生成V2.bat` | V2.0启动脚本 |
| `templates/phase_configs.py` | 施工阶段配置 |
| `templates/plan_configs.py` | 方案模板配置 |
| `templates/calculations.py` | 计算书生成器 |

---

## 🔗 相关项目

- 借鉴: [CAD-BIM-to-Code-Automation](https://github.com/datadrivenconstruction/CAD-BIM-to-Code-Automation-Pipeline-DDC-Workflow-with-LLM-ChatGPT)
- 借鉴: [bimflowsuite](https://github.com/Nnamdi-Oniya/bimflowsuite)
- 项目来源: 北车上盖学校方案编制清单（2025年11月26日）

---
**版本**: 3.0  
**更新日期**: 2026-03-17  
**作者**: 大虾 (基于 OpenClaw 框架)  
**项目**: 松岗街道北车上盖学校新建工程
