#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版施工方案编制大师 V2.0
支持可扩展的方案模板系统
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# 导入模板系统
from templates.plan_configs import get_template, list_templates, check_expert_required
from templates.calculations import ExtendedXlsxGenerator
from generators.ai_content import AIContentGenerator

class PlanGeneratorV2:
    """可扩展的施工方案生成器"""
    
    def __init__(self, output_dir=None):
        if output_dir is None:
            output_dir = Path.home() / "Documents" / "施工方案"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.xlsx_gen = ExtendedXlsxGenerator()
        self.ai_gen = AIContentGenerator()
    
    def generate_text_plan(self, project_info):
        """根据模板生成方案大纲"""
        plan_type = project_info.get('plan_type', '深基坑')
        template = get_template(plan_type)
        
        lines = []
        lines.append(f"{project_info.get('name', '工程')} {plan_type}施工方案")
        lines.append("=" * 60)
        lines.append(f"\n编制日期: {datetime.now().strftime('%Y年%m月%d日')}")
        lines.append(f"\n一、工程概况")
        lines.append(f"工程名称: {project_info.get('name', '未命名')}")
        lines.append(f"工程类型: {template['description']}")
        lines.append(f"建筑面积: {project_info.get('area', '待定')}㎡")
        lines.append(f"结构形式: {project_info.get('structure', '待定')}")
        
        # 根据方案类型显示特定参数
        if plan_type == "深基坑":
            lines.append(f"基坑深度: {project_info.get('depth', '待定')}m")
        elif plan_type in ["高支模", "脚手架"]:
            lines.append(f"搭设高度: {project_info.get('height', '待定')}m")
        elif plan_type == "塔吊基础":
            lines.append(f"塔吊型号: {project_info.get('tower_model', '待定')}")
        elif plan_type == "起重吊装":
            lines.append(f"构件重量: {project_info.get('weight', '待定')}kN")
        
        # 编制依据
        lines.append(f"\n二、编制依据")
        for code in template['codes']:
            lines.append(f"- {code}")
        
        # 危险源识别
        lines.append(f"\n三、危险源识别")
        hazards_str = " □ ".join(template['hazards'])
        lines.append(f"□ {hazards_str}")
        
        # 专家论证
        need_expert, reason = check_expert_required(plan_type, project_info)
        if need_expert or template['expert_threshold'] is None:
            lines.append(f"\n四、专家论证要求")
            lines.append(f"⚠ {reason}")
        
        # 计算书内容概述
        lines.append(f"\n五、计算书内容")
        for calc in template['calculations']:
            calc_names = {
                'earth_pressure': '土压力计算',
                'support_force': '支撑轴力计算',
                'scaffold_stability': '支架稳定性计算',
                'load_calculation': '荷载计算',
                'wind_load': '风荷载计算',
                'foundation_bearing': '地基承载力计算',
                'stability_check': '稳定性验算',
                'lifting_capacity': '起重能力验算',
                'rigging_check': '吊索具验算',
                'cable_selection': '电缆选型计算'
            }
            lines.append(f"- {calc_names.get(calc, calc)}")
        
        return "\n".join(lines)
    
    def generate_calculations(self, plan_type, project_info):
        """根据方案类型生成对应的计算书"""
        template = get_template(plan_type)
        calculations = template['calculations']
        
        # 深基坑计算
        if 'earth_pressure' in calculations or plan_type == '深基坑':
            calc_params = {
                'depth': project_info.get('depth', 10),
                'water_level': project_info.get('water_level', -2),
                'gamma': project_info.get('gamma', 18),
                'c': project_info.get('c', 20),
                'phi': project_info.get('phi', 20)
            }
            self.xlsx_gen.generate_earth_pressure_calc(calc_params)
            
            # 支撑计算（深基坑）
            if plan_type == '深基坑':
                supports = [
                    {'level': 1, 'elevation': -2.0, 'spacing': 6.0, 'force': 850},
                    {'level': 2, 'elevation': -6.0, 'spacing': 6.0, 'force': 1200},
                    {'level': 3, 'elevation': -9.0, 'spacing': 6.0, 'force': 950}
                ]
                self.xlsx_gen.generate_support_force_calc(supports)
        
        # 高支模计算
        if plan_type == '高支模' or 'scaffold_stability' in calculations:
            scaffold_params = {
                'height': project_info.get('height', 8),
                'spacing_long': 0.9,
                'spacing_trans': 0.9,
                'step': 1.5,
                'slab_thickness': project_info.get('slab_thickness', 200)
            }
            self.xlsx_gen.generate_scaffold_stability(scaffold_params)
        
        # 塔吊基础计算
        if plan_type == '塔吊基础' or 'foundation_bearing' in calculations:
            tower_params = {
                'tower_model': project_info.get('tower_model', 'TC5613'),
                'max_load': project_info.get('max_load', 6),
                'max_radius': project_info.get('max_radius', 56),
                'counterweight': project_info.get('counterweight', 12),
                'tower_weight': project_info.get('tower_weight', 45),
                'bearing_capacity': project_info.get('bearing_capacity', 150)
            }
            self.xlsx_gen.generate_tower_foundation(tower_params)
    
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
        self.xlsx_gen = ExtendedXlsxGenerator()  # 重置
        self.generate_calculations(plan_type, project_info)
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
    parser = argparse.ArgumentParser(description='增强版施工方案编制工具 V2.0')
    parser.add_argument('--name', default='测试工程', help='工程名称')
    parser.add_argument('--type', default='深基坑', 
                       choices=list_templates(),
                       help=f'方案类型，可选: {", ".join(list_templates())}')
    parser.add_argument('--area', default='50000', help='建筑面积(㎡)')
    parser.add_argument('--structure', default='框架核心筒', help='结构形式')
    
    # 深基坑参数
    parser.add_argument('--depth', type=float, default=12, help='基坑深度(m)')
    parser.add_argument('--water-level', type=float, default=-2, help='地下水位(m)')
    parser.add_argument('--gamma', type=float, default=18, help='土体重度(kN/m³)')
    parser.add_argument('--c', type=float, default=20, help='粘聚力(kPa)')
    parser.add_argument('--phi', type=float, default=20, help='内摩擦角(°)')
    
    # 高支模参数
    parser.add_argument('--height', type=float, default=0, help='搭设高度(m)')
    parser.add_argument('--slab-thickness', type=float, default=200, help='楼板厚度(mm)')
    
    # 塔吊参数
    parser.add_argument('--tower-model', default='TC5613', help='塔吊型号')
    parser.add_argument('--max-load', type=float, default=6, help='最大起重量(t)')
    parser.add_argument('--bearing-capacity', type=float, default=150, help='地基承载力(kPa)')
    
    # 起重吊装参数
    parser.add_argument('--weight', type=float, default=0, help='构件重量(kN)')
    
    args = parser.parse_args()
    
    project_info = {
        'name': args.name,
        'plan_type': args.type,
        'area': args.area,
        'structure': args.structure,
        # 深基坑
        'depth': args.depth,
        'water_level': args.water_level,
        'gamma': args.gamma,
        'c': args.c,
        'phi': args.phi,
        # 高支模
        'height': args.height if args.height > 0 else args.depth,  # 默认使用深度
        'slab_thickness': args.slab_thickness,
        # 塔吊
        'tower_model': args.tower_model,
        'max_load': args.max_load,
        'bearing_capacity': args.bearing_capacity,
        # 起重
        'weight': args.weight if args.weight > 0 else args.max_load * 10,
    }
    
    planner = PlanGeneratorV2()
    result = planner.generate_complete_plan(project_info)
    
    print("\n[输出] 生成的文件:")
    for key, path in result.items():
        print(f"  - {key}: {path}")
    
    # 显示专家论证要求
    need_expert, reason = check_expert_required(args.type, project_info)
    print(f"\n[论证] {reason}")

if __name__ == "__main__":
    main()
