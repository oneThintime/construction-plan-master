#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版施工方案编制大师 - 最终整合版 V4.0
集成: 单方案生成 + 多模板 + 按阶段批量生成
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# 导入生成器
from generators import AIContentGenerator, CalculationXlsxGenerator
from templates.plan_configs import get_template, list_templates, check_expert_required
from templates.phase_configs import (
    CONSTRUCTION_PHASES, get_phase_list, get_phase_info, 
    count_by_level, get_all_plans_count
)

class ConstructionPlanMaster:
    """施工方案编制大师 - 终极版"""
    
    def __init__(self, output_dir=None):
        if output_dir is None:
            output_dir = Path.home() / "Documents" / "施工方案"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.xlsx_gen = CalculationXlsxGenerator()
        self.ai_gen = AIContentGenerator()
    
    # ==================== 模式1: 单方案生成 ====================
    def generate_single_plan(self, project_info):
        """生成单个方案"""
        plan_type = project_info.get('plan_type', '深基坑')
        project_name = project_info.get('name', '新建工程')
        
        print(f"\n[模式: 单方案生成]")
        print(f"[开始] 正在生成 {project_name} 的 {plan_type} 施工方案...")
        
        # 1. 生成文本方案
        print("[步骤1] 正在生成方案大纲...")
        text_plan = self._generate_single_text(project_info)
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
        
        print(f"\n[成功] 方案生成完成！")
        return {
            'txt': str(txt_path),
            'xlsx': str(xlsx_path),
            'ai_prompt': str(ai_prompt_path)
        }
    
    def _generate_single_text(self, project_info):
        """生成单个方案文本"""
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
            lines.append("[提示] 本工程需组织专家论证（开挖深度≥5m）")
        
        return "\n".join(lines)
    
    # ==================== 模式2: 按阶段批量生成 ====================
    def list_phases(self):
        """列出所有施工阶段"""
        print("\n" + "=" * 70)
        print("施工方案编制大师 - 按施工阶段生成")
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
    
    def generate_phase_plans(self, phase_key, project_name="北车上盖学校"):
        """生成指定阶段的所有方案"""
        phase_info = get_phase_info(phase_key)
        if not phase_info:
            print(f"[错误] 未找到阶段 {phase_key}")
            return
        
        phase_name = phase_info['phase_name']
        plans = phase_info.get('plans', [])
        
        print(f"\n{'=' * 70}")
        print(f"【{phase_name}】方案生成")
        print(f"{'=' * 70}")
        print(f"本阶段共 {len(plans)} 个方案\n")
        
        # 创建阶段目录
        project_dir = self.output_dir / project_name.replace(' ', '_')
        phase_dir = project_dir / phase_key
        phase_dir.mkdir(parents=True, exist_ok=True)
        
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
            content = self._generate_phase_plan_outline(plan, project_name)
            
            # 保存文件
            filename = f"{i:02d}_{plan_type}_{plan_name[:20]}.txt"
            filename = filename.replace(' ', '_').replace('/', '-').replace('\\', '-')
            filepath = phase_dir / filename
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                generated.append(filepath)
            except Exception as e:
                print(f"   [警告] 保存失败 {filename}: {e}")
                continue
            
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
        print("=" * 70 + "\n")
        
        return {
            'phase': phase_name,
            'total': len(plans),
            'generated': generated,
            'urgent': urgent_list,
            'expert': expert_list,
            'dir': str(phase_dir)
        }
    
    def _generate_phase_plan_outline(self, plan, project_name):
        """生成阶段方案大纲"""
        lines = []
        lines.append(f"{plan['name']}")
        lines.append("=" * 70)
        lines.append(f"\n方案类别: {plan['type']}")
        lines.append(f"方案级别: {plan['level']}类")
        lines.append(f"紧急程度: {'[急]' if plan.get('urgent') else '[普]'}")
        
        if plan.get('expert_required'):
            lines.append(f"专家论证: [需论证]")
        
        lines.append(f"\n编制日期: {datetime.now().strftime('%Y年%m月%d日')}")
        lines.append(f"编制单位: {project_name}项目部")
        
        lines.append("\n" + "-" * 70)
        lines.append("【方案大纲】")
        lines.append("-" * 70)
        
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
    
    def generate_all_phases(self, project_name="北车上盖学校"):
        """生成所有阶段的方案"""
        print("\n" + "=" * 70)
        print("开始批量生成所有阶段方案...")
        print("=" * 70)
        
        results = []
        for phase_key in get_phase_list():
            result = self.generate_phase_plans(phase_key, project_name)
            if result:
                results.append(result)
        
        # 生成总汇总
        self._generate_master_summary(results, project_name)
        
        return results
    
    def _generate_master_summary(self, results, project_name):
        """生成总汇总文件"""
        project_dir = self.output_dir / project_name.replace(' ', '_')
        summary_path = project_dir / "_项目方案总清单.txt"
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(f"{project_name}项目 - 施工方案总清单\n")
            f.write("=" * 70 + "\n")
            f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
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

def interactive_menu():
    """交互式菜单"""
    print("\n" + "=" * 70)
    print("施工方案编制大师 V4.0")
    print("=" * 70)
    print("\n请选择工作模式:")
    print("\n  [1] 单方案生成 - 生成单个危大工程方案（含计算书）")
    print("  [2] 按阶段生成 - 按施工阶段批量生成（北车上盖学校项目）")
    print("  [3] 查看阶段列表 - 显示所有施工阶段信息")
    print("  [4] 生成所有阶段 - 一次性生成全部133个方案")
    print("  [0] 退出")
    print("\n" + "=" * 70)
    return input("\n请输入选项 [0-4]: ")

def main():
    parser = argparse.ArgumentParser(description='施工方案编制大师 V4.0')
    parser.add_argument('--mode', choices=['single', 'phase', 'list', 'all'], 
                       help='工作模式: single=单方案, phase=按阶段, list=查看阶段, all=全部')
    parser.add_argument('--name', default='新建工程', help='工程名称')
    parser.add_argument('--type', default='深基坑', choices=list_templates(),
                       help=f'方案类型: {", ".join(list_templates())}')
    parser.add_argument('--phase', type=int, help='指定阶段 (1-7)')
    parser.add_argument('--depth', type=float, default=12, help='基坑深度(m)')
    parser.add_argument('--area', default='50000', help='建筑面积(㎡)')
    parser.add_argument('--structure', default='框架核心筒', help='结构形式')
    
    args = parser.parse_args()
    
    master = ConstructionPlanMaster()
    
    # 命令行模式
    if args.mode:
        if args.mode == 'single':
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
            master.generate_single_plan(project_info)
            
        elif args.mode == 'phase' and args.phase:
            phase_keys = get_phase_list()
            if 1 <= args.phase <= len(phase_keys):
                master.generate_phase_plans(phase_keys[args.phase - 1], args.name)
            else:
                print(f"[错误] 阶段编号应为 1-{len(phase_keys)}")
                
        elif args.mode == 'list':
            master.list_phases()
            
        elif args.mode == 'all':
            master.generate_all_phases(args.name)
    else:
        # 交互式菜单模式
        while True:
            choice = interactive_menu()
            
            if choice == '1':
                print("\n" + "=" * 70)
                print("[模式: 单方案生成]")
                name = input("工程名称 [新建工程]: ") or "新建工程"
                print(f"\n可用方案类型: {', '.join(list_templates())}")
                plan_type = input("方案类型 [深基坑]: ") or "深基坑"
                depth = float(input("基坑深度 [12]: ") or "12")
                
                project_info = {
                    'name': name,
                    'plan_type': plan_type,
                    'area': '50000',
                    'structure': '框架核心筒',
                    'depth': depth,
                    'floors': '地下3层/地上30层',
                    'water_level': -2,
                    'gamma': 19,
                    'c': 25,
                    'phi': 18
                }
                master.generate_single_plan(project_info)
                input("\n按回车键继续...")
                
            elif choice == '2':
                print("\n" + "=" * 70)
                print("[模式: 按阶段生成]")
                master.list_phases()
                phase_num = input("\n请选择阶段 [1-7]: ")
                if phase_num.isdigit():
                    phase_keys = get_phase_list()
                    if 1 <= int(phase_num) <= len(phase_keys):
                        master.generate_phase_plans(phase_keys[int(phase_num) - 1])
                input("\n按回车键继续...")
                
            elif choice == '3':
                master.list_phases()
                input("\n按回车键继续...")
                
            elif choice == '4':
                confirm = input("\n确定要生成全部133个方案吗？(y/n): ")
                if confirm.lower() == 'y':
                    master.generate_all_phases()
                input("\n按回车键继续...")
                
            elif choice == '0':
                print("\n感谢使用，再见！\n")
                break

if __name__ == "__main__":
    main()
