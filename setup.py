from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="construction-plan-master",
    version="4.0.0",
    author="大虾 (Da Xia)",
    author_email="your-email@example.com",
    description="施工方案编制大师 - A comprehensive construction engineering plan generation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/construction-plan-master",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Construction Industry",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: Chinese (Simplified)",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "construction-plan=construction_plan_master:main",
        ],
    },
)
