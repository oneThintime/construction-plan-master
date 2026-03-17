# Contributing to Construction Plan Master

Thank you for your interest in contributing to Construction Plan Master! This document provides guidelines and instructions for contributing.

## 🌟 Ways to Contribute

### 1. Report Issues
- Bug reports
- Feature requests
- Documentation improvements

### 2. Code Contributions
- New plan templates
- New calculation modules
- UI/UX improvements
- Performance optimizations

### 3. Documentation
- Translation (English/Chinese)
- Usage examples
- Tutorial videos

## 📝 Before You Start

### Prerequisites
- Python 3.8+
- Windows 10/11 (for testing)
- Git

### Setup Development Environment

```bash
# Fork the repository
# Clone your fork
git clone https://github.com/YOUR_USERNAME/construction-plan-master.git

# Create a virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest flake8 black
```

## 🔧 Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Make Your Changes
- Follow PEP 8 style guide
- Add docstrings to functions
- Update relevant documentation
- Add tests for new features

### 3. Test Your Changes
```bash
# Run tests
pytest

# Check code style
flake8 .

# Format code
black .
```

### 4. Commit Your Changes
```bash
git add .
git commit -m "feat: add new feature description"
```

**Commit Message Format:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Build process or auxiliary tool changes

### 5. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## 📋 Pull Request Guidelines

### PR Checklist
- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No merge conflicts

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
Describe the tests you ran

## Screenshots (if applicable)
Add screenshots for UI changes

## Related Issues
Fixes #(issue number)
```

## 🏗️ Adding New Plan Types

### Step 1: Add Template Configuration
Edit `templates/plan_configs.py`:

```python
"New Plan Type": {
    "description": "Description",
    "expert_threshold": {
        "param": "depth",
        "value": 5,
        "unit": "m"
    },
    "codes": [
        "《规范名称》GB XXXXX-20XX"
    ],
    "hazards": ["坍塌", "高处坠落"],
    "calculations": ["calc_type"],
    "required_params": ["depth", "area"],
    "ai_sections": ["工程概况", "施工工艺"]
}
```

### Step 2: Add Calculation Module (if needed)
Edit `templates/calculations.py`:

```python
def generate_new_calculation(self, params):
    """New calculation description"""
    ws = self.wb.create_sheet(title="新计算")
    # Calculation logic here
    return self.wb
```

### Step 3: Add Section Structure
```python
def _get_sections_by_type(self, plan_type):
    sections_map = {
        "New Type": [
            "编制依据",
            "工程概况",
            "施工工艺",
            "安全措施"
        ]
    }
```

### Step 4: Test
```bash
python construction_plan_master.py --mode single --name "Test" --type "New Plan Type"
```

## 🌍 Translation Guidelines

### Adding New Language Support
1. Create `README_LANG.md` (e.g., `README_JP.md` for Japanese)
2. Translate key terms consistently
3. Update main README with language link

### Key Terminology
| English | Chinese |
|---------|---------|
| Deep Excavation | 深基坑 |
| High Formwork | 高支模 |
| Expert Review | 专家论证 |
| Hazardous Project | 危大工程 |
| Construction Plan | 施工方案 |

## 🐛 Bug Report Template

```markdown
**Describe the bug**
A clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Run command '...'
2. Enter input '...'
3. See error

**Expected behavior**
What you expected to happen

**Screenshots**
If applicable

**Environment:**
- OS: [e.g. Windows 11]
- Python version: [e.g. 3.10]
- Version: [e.g. 4.0]

**Additional context**
Any other context
```

## 💡 Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of what the problem is

**Describe the solution you'd like**
A clear description of what you want

**Describe alternatives you've considered**
Any alternative solutions

**Additional context**
Any other context or screenshots
```

## 📝 Code Style Guidelines

### Python Style
- Follow PEP 8
- Maximum line length: 100 characters
- Use meaningful variable names
- Add type hints where appropriate

### Documentation Style
- Use clear, concise language
- Provide examples
- Keep README updated

### Example Code Style
```python
def generate_plan(project_info: dict) -> dict:
    """
    Generate construction plan based on project info.
    
    Args:
        project_info: Dictionary containing project parameters
        
    Returns:
        Dictionary containing generated file paths
    """
    # Implementation
    pass
```

## 🎯 Development Priorities

### High Priority
- Security fixes
- Critical bug fixes
- Performance improvements

### Medium Priority
- New plan templates
- UI improvements
- Documentation

### Low Priority
- Code refactoring
- Minor optimizations

## 📞 Contact

- GitHub Issues: [Report issues here](../../issues)
- Pull Requests: [Submit PRs here](../../pulls)
- Email: [your-email@example.com]

## 🙏 Thank You!

Your contributions make this project better for everyone!

---

**Note**: By contributing to this project, you agree that your contributions will be licensed under the MIT License.
