from setuptools import setup, find_packages

Hypen_e_dot = "-e ."
# This is the file where we will be creating the setup.py file for our project.

requirements=[]
def get_requirements(file_path):
    """This function returns a list of requirements from the given file."""
    with open(file_path) as file:
        requiremnets=file.readlines()
        for req in requiremnets:
            req=req.replace("\n","")
            requirements.append(req)
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)    

setup(
    name="mlproject",
    version="0.0.1",
    author="Yash",
    author_email="yaswanthreddy@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
)