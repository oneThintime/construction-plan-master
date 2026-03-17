#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
按施工阶段批量生成方案 V3.0
北车上盖学校项目专用
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

from templates.phase_configs import (
    CONSTRUCTION_PHASES, get_phase_list, get_phase_info, 
    count_by_level, get_all_plans_count
)
from templates.plan_configs import check_expert_required

class PhasePlanGenerator:
    """按施工阶段生成方案"""
    
    def __init__(self, output_dir=None):
        if output_dir is None:
            output_dir = Path.home() / "Documents" / "施工方案" / "北车上盖学校"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def list_phases(self):
        """列出所有施工阶段"""
        print("\n" + "=" * 70)
        print("北车上盖学校项目 - 施工阶段划分")
        print("=" * 70)
        
        for i, (phase_key, phase_info) in enumerate(CONSTRUCTION_PHASES.items(), 1):
            plan_count = len(phase_info.get("plans", []))
            urgent_count = sum(1 for p in phase_info["plans"] if p.get("urgent"))
            expert_count = sum(1 for p in phase_info["plans"] if p.get("expert_required"))
            
            print(f"\n【阶段{i}】{phase_info['phase_name']}")
            print(f"    时间: {phase_info['time_range']}")
            print(f"    说明: {phase_info['description']}")
            print(f"    方案数: {plan_count}个 (紧急{urgent_count}个, 需论证{expert_count}个)")
        
        print(f"\n{'=' * 70}")
        print(f"总计: {get_all_plans_count()}个方案")
        
        level_count = count_by_level()
        print(f"按级别: A类(专家论证) {level_count.get('A', 0)}个, "
              f"B类(危大工程) {level_count.get('B', 0)}个, "
              f"C类(一般安全) {level_count.get('C', 0)}个, "
              f"D类(普通方案) {level_count.get('D', 0)}个")
        print("=" * 70 + "\n")
    
    def generate_phase_plans(self, phase_key, project_info=None):
        """生成指定阶段的所有方案大纲"""
        phase_info = get_phase_info(phase_key)
        if not phase_info:
            print(f"错误: 未找到阶段 {phase_key}")
            return
        
        phase_name = phase_info['phase_name']
        plans = phase_info.get('plans', [])
        
        print(f"\n{'=' * 70}")
        print(f"【{phase_name}】方案生成")
        print(f"{'=' * 70}")
        print(f"本阶段共 {len(plans)} 个方案\n")
        
        # 创建阶段目录
        phase_dir = self.output_dir / phase_key
        phase_dir.mkdir(exist_ok=True)
        
        generated = []
        urgent_list = []
        expert_list = []
        
        for i, plan in enumerate(plans, 1):
            plan_name = plan['name']
            plan_type = plan['type']
            plan_level = plan['level']
            is_urgent = plan.get('urgent', False)
            need_expert = plan.get('expert_required', False)
            
            # 生成方案大纲
            content = self._generate_plan_outline(plan, project_info)
            
            # 保存文件
            filename = f"{i:02d}_{plan_type}_{plan_name[:20]}.txt"
            filename = filename.replace(' ', '_').replace('/', '-')
            filepath = phase_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            generated.append(filepath)
            
            if is_urgent:
                urgent_list.append(plan)
            if need_expert:
                expert_list.append(plan)
            
            status = ""
            if need_expert:
                status += " [需专家论证]"
            elif plan_level in ['A', 'A/B']:
                status += " [危大工程]"
            
            print(f"  [{i}/{len(plans)}] {plan_name[:40]}... - 完成{status}")
        
        # 生成阶段汇总文件
        summary_path = phase_dir / "_阶段方案汇总.txt"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(f"{phase_name} - 方案编制清单\n")
            f.write("=" * 70 + "\n")
            f.write(f"阶段时间: {phase_info['time_range']}\n")
            f.write(f"阶段说明: {phase_info['description']}\n")
            f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write("=" * 70 + "\n\n")
            
            f.write(f"【紧急优先方案】共{len(urgent_list)}个\n")
            for p in urgent_list:
                f.write(f"  [急] {p['name']} ({p['level']}类)\n")
            
            f.write(f"\n【需专家论证方案】共{len(expert_list)}个\n")
            for p in expert_list:
                f.write(f"  [证] {p['name']} ({p['level']}类)\n")
            
            f.write(f"\n【全部方案清单】共{len(plans)}个\n")
            for i, p in enumerate(plans, 1):
                urgent_mark = "急" if p.get('urgent') else " "
                expert_mark = "证" if p.get('expert_required') else " "
                f.write(f"  {i:2d}. [{urgent_mark}{expert_mark}] {p['name']} - {p['level']}类\n")
        
        print(f"\n{'=' * 70}")
        print(f"[完成] 已生成 {len(generated)} 个方案文件")
        print(f"[完成] 紧急方案: {len(urgent_list)} 个")
        print(f"[完成] 需论证方案: {len(expert_list)} 个")
        print(f"[完成] 输出目录: {phase_dir}")
        print(f"[完成] 汇总文件: {summary_path}")
        print("=" * 70 + "\n")
        
        return {
            'phase': phase_name,
            'total': len(plans),
            'generated': generated,
            'urgent': urgent_list,
            'expert': expert_list,
            'dir': str(phase_dir)
        }
    
    def _generate_plan_outline(self, plan, project_info):
        """生成单个方案的大纲"""
        lines = []
        lines.append(f"{plan['name']}")
        lines.append("=" * 70)
        lines.append(f"\n方案类别: {plan['type']}")
        lines.append(f"方案级别: {plan['level']}类")
        lines.append(f"紧急程度: {'[急]' if plan.get('urgent') else '[普]'}")
        
        if plan.get('expert_required'):
            lines.append(f"专家论证: [需论证]")
        
        lines.append(f"\n编制日期: {datetime.now().strftime('%Y年%m月%d日')}")
        lines.append(f"编制单位: 北车上盖学校项目部")
        
        lines.append("\n" + "-" * 70)
        lines.append("【方案大纲】")
        lines.append("-" * 70)
        
        # 根据方案类型生成不同大纲
        sections = self._get_sections_by_type(plan['type'])
        for i, section in enumerate(sections, 1):
            lines.append(f"\n{i}. {section}")
        
        lines.append("\n" + "-" * 70)
        lines.append("【编制依据】")
        lines.append("-" * 70)
        lines.append("- 《建筑工程施工质量验收统一标准》GB 50300-2013")
        lines.append("- 本项目施工合同、设计图纸")
        lines.append("- 相关法律、法规及规范")
        
        return "\n".join(lines)
    
    def _get_sections_by_type(self, plan_type):
        """根据方案类型返回章节结构"""
        sections_map = {
            "策划类": ["编制说明", "工程概况", "总体部署", "施工进度计划", "资源配置", "质量保证措施", "安全保证措施"],
            "临建类": ["编制依据", "临建布置", "临建结构", "临水临电", "安全措施", "环保措施"],
            "土方基坑": ["编制依据", "工程地质", "基坑支护", "土方开挖", "降排水", "监测方案", "应急预案"],
            "塔吊": ["编制依据", "塔吊选型", "基础设计", "安装工艺", "安全措施", "应急预案"],
            "垂直运输": ["编制依据", "设备选型", "基础设计", "安装拆除", "安全措施"],
            "起重吊装": ["编制依据", "吊装工艺", "吊索具计算", "安全措施", "应急预案"],
            "混凝土": ["编制依据", "混凝土配合比", "浇筑工艺", "养护措施", "质量控制"],
            "钢筋": ["编制依据", "钢筋加工", "钢筋连接", "钢筋安装", "质量标准"],
            "模板": ["编制依据", "模板设计", "模板安装", "模板拆除", "安全措施"],
            "脚手架": ["编制依据", "架体设计", "搭设工艺", "验收标准", "安全措施"],
            "防水": ["编制依据", "防水材料", "施工工艺", "细部处理", "质量验收"],
            "隔墙": ["编制依据", "材料要求", "施工工艺", "质量标准"],
            "装修": ["编制依据", "施工顺序", "主要工序", "质量标准", "成品保护"],
            "机电综合": ["编制依据", "系统概况", "施工部署", "主要工序", "调试方案"],
            "监测检测": ["编制依据", "监测内容", "监测方法", "数据处理", "预警机制"],
            "其他": ["编制依据", "工程概况", "施工部署", "技术措施", "安全措施", "应急预案"],
        }
        return sections_map.get(plan_type, sections_map["其他"])
    
    def generate_all_phases(self, project_info=None):
        """生成所有阶段的方案"""
        print("\n" + "=" * 70)
        print("开始批量生成所有阶段方案...")
        print("=" * 70)
        
        results = []
        for phase_key in get_phase_list():
            result = self.generate_phase_plans(phase_key, project_info)
            results.append(result)
        
        # 生成总汇总
        self._generate_master_summary(results)
        
        return results
    
    def _generate_master_summary(self, results):
        """生成总汇总文件"""
        summary_path = self.output_dir / "_项目方案总清单.txt"
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("北车上盖学校项目 - 施工方案总清单\n")
            f.write("=" * 70 + "\n")
            f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"项目概况: 松岗街道北车上盖保障房配套九年制学校新建工程\n")
            f.write("=" * 70 + "\n\n")
            
            total_plans = sum(r['total'] for r in results)
            total_urgent = sum(len(r['urgent']) for r in results)
            total_expert = sum(len(r['expert']) for r in results)
            
            f.write("【统计汇总】\n")
            f.write(f"  方案总数: {total_plans}个\n")
            f.write(f"  紧急方案: {total_urgent}个\n")
            f.write(f"  需论证方案: {total_expert}个\n\n")
            
            f.write("【各阶段统计】\n")
            for r in results:
                f.write(f"\n{r['phase']}\n")
                f.write(f"  方案数: {r['total']}个\n")
                f.write(f"  紧急: {len(r['urgent'])}个, 需论证: {len(r['expert'])}个\n")
                f.write(f"  目录: {r['dir']}\n")
            
            f.write("\n" + "=" * 70 + "\n")
            f.write("【需专家论证方案清单】\n")
            f.write("=" * 70 + "\n\n")
            
            expert_no = 1
            for r in results:
                if r['expert']:
                    f.write(f"\n{r['phase']}:\n")
                    for p in r['expert']:
                        f.write(f"  {expert_no}. {p['name']} ({p['level']}类)\n")
                        expert_no += 1
        
        print(f"\n{'=' * 70}")
        print(f"[完成] 项目总清单已生成: {summary_path}")
        print("=" * 70 + "\n")

def main():
    parser = argparse.ArgumentParser(description='按施工阶段生成方案 V3.0')
    parser.add_argument('--list', action='store_true', help='列出所有阶段')
    parser.add_argument('--phase', type=int, help='生成指定阶段 (1-7)')
    parser.add_argument('--all', action='store_true', help='生成所有阶段')
    parser.add_argument('--name', default='北车上盖学校', help='项目名称')
    
    args = parser.parse_args()
    
    generator = PhasePlanGenerator()
    
    if args.list:
        generator.list_phases()
    elif args.phase:
        phase_keys = get_phase_list()
        if 1 <= args.phase <= len(phase_keys):
            project_info = {'name': args.name}
            generator.generate_phase_plans(phase_keys[args.phase - 1], project_info)
        else:
            print(f"错误: 阶段编号应为 1-{len(phase_keys)}")
    elif args.all:
        project_info = {'name': args.name}
        generator.generate_all_phases(project_info)
    else:
        # 默认显示帮助
        generator.list_phases()
        print("\n使用方法:")
        print("  python phase_generator_v3.py --list       # 查看所有阶段")
        print("  python phase_generator_v3.py --phase 1    # 生成阶段1")
        print("  python phase_generator_v3.py --all        # 生成所有阶段")

if __name__ == "__main__":
    main()
