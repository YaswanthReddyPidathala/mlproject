from setuptools import setup, find_packages

Hypen_e_dot = "-e ."
# This is the file where we will be creating the setup.py file for our project.

with open("readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()




setup(
    name="mlproject",
    version="0.0.1",
    author="Yash",
    author_email="yaswanthreddy@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)