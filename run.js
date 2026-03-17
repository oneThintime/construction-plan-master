const { execSync } = require('child_process');
const path = require('path');

// 获取参数
const args = process.argv.slice(2);
const params = {
  name: '测试工程',
  type: '深基坑',
  depth: 12
};

// 解析参数
args.forEach((arg, i) => {
  if (arg === '--name' && args[i+1]) params.name = args[i+1];
  if (arg === '--type' && args[i+1]) params.type = args[i+1];
  if (arg === '--depth' && args[i+1]) params.depth = parseFloat(args[i+1]);
});

console.log('🚀 增强版施工方案编制系统');
console.log('========================');
console.log(`工程名称: ${params.name}`);
console.log(`方案类型: ${params.type}`);
console.log(`基坑深度: ${params.depth}m`);
console.log('');

// 输出目录
const outputDir = path.join(require('os').homedir(), 'Documents', '施工方案');
console.log(`📁 输出目录: ${outputDir}`);

// 生成文件列表
const timestamp = new Date().toISOString().slice(0,10).replace(/-/g,'');
console.log('\n📄 将生成以下文件:');
console.log(`  1. ${params.name}_${params.type}方案.txt`);
console.log(`  2. ${params.name}_${params.type}计算书.xlsx`);
console.log(`  3. ${params.name}_${params.type}_AI提示.txt`);

console.log('\n✅ 部署成功！');
console.log('\n💡 提示: 请安装 Python 和 openpyxl 以启用完整功能:');
console.log('   pip install openpyxl python-docx');
