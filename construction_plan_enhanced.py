#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版施工方案编制大师
集成: Excel计算书 + AI内容 + 文档生成
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# 导入生成器
from generators import AIContentGenerator, CalculationXlsxGenerator

class EnhancedConstructionPlan:
    """增强版施工方案编制系统"""
    
    def __init__(self, output_dir=None):
        if output_dir is None:
            output_dir = Path.home() / "Documents" / "施工方案"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.xlsx_gen = CalculationXlsxGenerator()
        self.ai_gen = AIContentGenerator()
        
    def generate_text_plan(self, project_info):
        """生成文本版方案大纲"""
        lines = []
        lines.append(f"{project_info.get('name', '工程')} {project_info.get('plan_type', '深基坑')}施工方案")
        lines.append("=" * 60)
        lines.append(f"\n编制日期: {datetime.now().strftime('%Y年%m月%d日')}")
        lines.append(f"\n一、工程概况")
        lines.append(f"工程名称: {project_info.get('name', '未命名')}")
        lines.append(f"建筑面积: {project_info.get('area', '待定')}㎡")
        lines.append(f"结构形式: {project_info.get('structure', '待定')}")
        lines.append(f"基坑深度: {project_info.get('depth', '待定')}m")
        
        lines.append(f"\n二、编制依据")
        codes = [
            "《建筑深基坑工程施工安全技术规范》JGJ 311-2013",
            "《建筑基坑工程监测技术标准》GB 50497-2019",
            "《建筑基坑支护技术规程》JGJ 120-2012"
        ]
        for code in codes:
            lines.append(f"- {code}")
        
        lines.append(f"\n三、危险源识别")
        lines.append("□ 坍塌 □ 高处坠落 □ 物体打击 □ 机械伤害 □ 触电")
        
        if project_info.get('depth', 0) >= 5:
            lines.append(f"\n四、专家论证要求")
            lines.append("⚠️ 本工程需组织专家论证（开挖深度≥5m）")
        
        return "\n".join(lines)
        
    def generate_complete_plan(self, project_info):
        """生成完整方案包"""
        plan_type = project_info.get('plan_type', '深基坑')
        project_name = project_info.get('name', '新建工程')
        
        print(f"[开始] 正在生成 {project_name} 的 {plan_type} 施工方案...")
        
        # 1. 生成文本方案
        print("[步骤1] 正在生成方案大纲...")
        text_plan = self.generate_text_plan(project_info)
        txt_path = self.output_dir / f"{project_name}_{plan_type}方案.txt"
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text_plan)
        print(f"   [完成] 已保存: {txt_path}")
        
        # 2. 生成 Excel 计算书
        print("[步骤2] 正在生成 Excel 计算书...")
        calc_params = {
            'depth': project_info.get('depth', 10),
            'water_level': project_info.get('water_level', -2),
            'gamma': project_info.get('gamma', 18),
            'c': project_info.get('c', 20),
            'phi': project_info.get('phi', 20)
        }
        self.xlsx_gen.generate_earth_pressure_calc(calc_params)
        
        # 添加支撑计算
        supports = [
            {'level': 1, 'elevation': -2.0, 'spacing': 6.0, 'force': 850},
            {'level': 2, 'elevation': -6.0, 'spacing': 6.0, 'force': 1200},
            {'level': 3, 'elevation': -9.0, 'spacing': 6.0, 'force': 950}
        ]
        self.xlsx_gen.generate_support_force_calc(supports)
        
        xlsx_path = self.output_dir / f"{project_name}_{plan_type}计算书.xlsx"
        self.xlsx_gen.save(str(xlsx_path))
        print(f"   [完成] 已保存: {xlsx_path}")
        
        # 3. 生成 AI 辅助内容提示
        print("[步骤3] 正在准备 AI 内容生成提示...")
        ai_contents = self.ai_gen.generate_full_plan_outline(project_info)
        ai_prompt_path = self.output_dir / f"{project_name}_{plan_type}_AI提示.txt"
        with open(ai_prompt_path, 'w', encoding='utf-8') as f:
            for content in ai_contents:
                f.write(f"{'='*60}\n")
                f.write(f"【{content['section_type']}】\n")
                f.write(f"{'='*60}\n")
                f.write(content['prompt'])
                f.write("\n\n")
        print(f"   [完成] 已保存: {ai_prompt_path}")
        
        print(f"\n[成功] 方案生成完成！输出目录: {self.output_dir}")
        return {
            'txt': str(txt_path),
            'xlsx': str(xlsx_path),
            'ai_prompt': str(ai_prompt_path)
        }

def main():
    parser = argparse.ArgumentParser(description='增强版施工方案编制工具')
    parser.add_argument('--name', default='测试工程', help='工程名称')
    parser.add_argument('--type', default='深基坑', help='方案类型')
    parser.add_argument('--area', default='50000', help='建筑面积')
    parser.add_argument('--structure', default='框架核心筒', help='结构形式')
    parser.add_argument('--depth', type=float, default=12, help='基坑深度')
    
    args = parser.parse_args()
    
    project_info = {
        'name': args.name,
        'plan_type': args.type,
        'area': args.area,
        'structure': args.structure,
        'depth': args.depth,
        'floors': '地下3层/地上30层',
        'water_level': -2,
        'gamma': 19,
        'c': 25,
        'phi': 18
    }
    
    planner = EnhancedConstructionPlan()
    result = planner.generate_complete_plan(project_info)
    
    print("\n[输出] 生成的文件:")
    for key, path in result.items():
        print(f"  - {key}: {path}")

if __name__ == "__main__":
    main()
