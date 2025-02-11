from setuptools import setup, find_packages # type: ignore

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="project_01",
    version="0.0.1",
    author="Kauê Siqueira",
    author_email="siqueiraprogrammer@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)