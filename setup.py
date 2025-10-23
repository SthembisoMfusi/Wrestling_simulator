"""
Setup script for the Wrestling Simulator package.
"""

from setuptools import setup, find_packages
import os


# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()


# Read requirements
def read_requirements():
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            requirements = [
                line.strip() for line in fh if line.strip() and not line.startswith("#")
            ]
            return requirements if requirements else []
    except FileNotFoundError:
        return []


setup(
    name="wrestling-simulator",
    version="1.0.1",
    author="Sthembiso Mfusi",
    author_email="sthembiso.mfusi@example.com",
    description="A Python-based wrestling tournament simulation game",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/SthembisoMfusi/Wrestling_simulator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "wrestling-simulator=wrestling_simulator.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "wrestling_simulator": ["data/*.txt"],
    },
)
