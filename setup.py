from setuptools import find_packages,setup
from pathlib import Path

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
__version__="0.0.0"

REPO_NAME="End-to-End-Chicken-Disease-Classification"
AUTHOR_USER_NAME="Bavan-M"
SRC_REPO="cnnProject"
AUTHOR_EMAIL="bavanreddy1999@gmail.com"
README=(Path(__file__).parent/"README.md").read_text(encoding="utf-8")

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
)

# This is a setup.py file, which is used to define Python package metadata and configuration for packaging and distribution. Let me break down each part of this setup() function call:

# Basic Metadata:
# name=SRC_REPO: The name of your package (likely defined as a variable elsewhere)
# version=__version__: The package version (also defined elsewhere)
# author=AUTHOR_USER_NAME: The author's name (likely your GitHub username)
# author_email=AUTHOR_EMAIL: The author's email address

# Description:
# description=...: A short one-line description of your package
# long_description=long_description: A detailed description (usually loaded from README.md)
# long_description_content_type="text/markdown": Specifies the long description is in Markdown format

# Project URLs:
# url=...: The main URL for your project (GitHub repo in this case)
# project_urls: Additional relevant URLs (here just showing the bug tracker)

# Package Structure:
# package_dir={"":"src"}: Tells setuptools that your packages are under the src directory
# packages=find_packages(where="src"): Automatically finds all Python packages in the src directory