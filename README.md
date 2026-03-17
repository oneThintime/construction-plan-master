

---

## 📸 Screenshots & Examples

### Interactive Menu Mode
```
========================================
      施工方案编制大师 V4.0
  Construction Plan Master
========================================

请选择操作模式:

1. 单方案生成模式 (Single Plan Mode)
   - 生成单个危大工程完整方案
   - 包含计算书、AI提示

2. 阶段批量生成模式 (Phase Mode)
   - 按7个施工阶段批量生成
   - 共133个方案

3. 生成全部方案 (Generate All)
   - 一键生成所有方案

请输入选项 (1-3):
```

### Generated Output Examples

#### Single Plan Output Structure
```
深基坑示范工程_深基坑方案.txt          # 方案大纲
深基坑示范工程_深基坑计算书.xlsx       # Excel计算书
深基坑示范工程_深基坑_AI提示.txt       # AI提示词
```

#### Phase Mode Output Structure
```
北车上盖学校/
├── 阶段1_施工准备/
│   ├── 01_策划类_施工组织设计.txt
│   ├── 02_策划类_质量策划书.txt
│   └── _阶段方案汇总.txt
├── 阶段2_桩基及基坑/
│   ├── 深基坑支护及土方开挖方案.txt
│   ├── 人工挖孔桩专项施工方案.txt
│   └── _阶段方案汇总.txt
├── ... (其他阶段)
└── _项目方案总清单.txt
```

### Sample Plan Content Preview

#### Deep Excavation Plan (深基坑方案)
```markdown
# 深基坑支护及土方开挖施工方案

## 一、工程概况
- 工程名称: 示例工程
- 基坑深度: 12m
- 基坑面积: 5000㎡
- 支护形式: 排桩+内支撑

## 二、编制依据
- JGJ 311-2013 建筑深基坑工程施工安全技术规范
- GB 50497-2019 建筑基坑工程监测技术标准

## 三、施工计划
[详细施工进度计划...]

## 四、施工工艺技术
[技术参数和施工方法...]

## 五、施工安全保证措施
[安全管理和应急预案...]

## 六、施工管理及作业人员配备
[组织架构和人员分工...]

## 七、验收要求
[验收标准和程序...]

## 八、应急处置措施
[应急预案和救援方案...]

## 九、计算书及相关图纸
[支撑计算、稳定性分析...]
```

### Excel Calculation Sheet Preview

#### Sheet 1: 土压力计算
| 参数 | 数值 | 单位 |
|------|------|------|
| 基坑深度 | 12.0 | m |
| 土体重度 | 18.5 | kN/m³ |
| 内摩擦角 | 25 | ° |
| 粘聚力 | 15 | kPa |
| 主动土压力系数 | 0.406 | - |
| 主动土压力 | 89.5 | kN/m |

#### Sheet 2: 支撑轴力计算
| 支撑层数 | 深度(m) | 水平间距(m) | 轴力(kN) |
|----------|---------|-------------|----------|
| 第1道 | 3.0 | 6.0 | 358 |
| 第2道 | 6.0 | 6.0 | 478 |
| 第3道 | 9.0 | 6.0 | 542 |

---

## 🎥 Video Tutorial (Coming Soon)

We are preparing video tutorials to help you get started:
- [ ] Installation Guide
- [ ] Single Plan Generation
- [ ] Phase-based Batch Generation
- [ ] Custom Template Creation
- [ ] Integration with PKPM

---

## 💡 Tips & Best Practices

### For Beginners
1. Start with **Single Plan Mode** to understand the output format
2. Use the default templates before creating custom ones
3. Check the generated calculation sheets carefully

### For Advanced Users
1. Customize `templates/plan_configs.py` for your specific needs
2. Modify `templates/phase_configs.py` to match your project phases
3. Use AI prompts to enhance generated content

### Common Issues & Solutions

#### Issue: Python not found
**Solution**: Install Python 3.8+ and add it to PATH, or run `配置环境.bat`

#### Issue: Excel generation fails
**Solution**: Install openpyxl: `pip install openpyxl`

#### Issue: Chinese characters display incorrectly
**Solution**: Ensure your terminal uses UTF-8 encoding

---

## 🔗 Quick Links

- [📖 Full Documentation](https://github.com/oneThintime/construction-plan-master/wiki)
- [🐛 Report Bug](https://github.com/oneThintime/construction-plan-master/issues/new?template=bug_report.md)
- [💡 Request Feature](https://github.com/oneThintime/construction-plan-master/issues/new?template=feature_request.md)
- [📧 Contact Author](mailto:your-email@example.com)

---

<div align="center">

**Made with ❤️ by 大虾 (Da Xia)**

[![GitHub stars](https://img.shields.io/github/stars/oneThintime/construction-plan-master?style=social)](https://github.com/oneThintime/construction-plan-master/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/oneThintime/construction-plan-master?style=social)](https://github.com/oneThintime/construction-plan-master/forks)

</div>
