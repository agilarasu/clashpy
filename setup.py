from setuptools import setup, find_packages

setup(
    name="clashpy",
    version="0.1.0",
    description="A Python package to interact with the Clash of Clans API",
    author="Agilarasu",
    author_email="s.agilarasu@outlook.com",
    packages=find_packages(),
    install_requires=["requests"],  # List your package dependencies
)
