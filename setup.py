from setuptools import setup, find_packages

# Define your long description (typically in a separate README file)
with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="clashpy",
    version="1.0.2",
    description="A Python package to interact with the Clash of Clans API",
    long_description=long_description,  # Use the README as long description
    long_description_content_type="text/markdown",  # Specify the content type
    author="Agilarasu",
    author_email="s.agilarasu@outlook.com",
    packages=find_packages(),
    url="https://github.com/agilarasu/clashpy",  # Provide a link to your GitHub repository
    project_urls={
        "Documentation": "https://github.com/agilarasu/clashpy/docs",
        "Bug Tracker": "https://github.com/agilarasu/clashpy/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="clashpy, Clash of Clans, API",
    install_requires=["requests"],  # List your package dependencies
    python_requires=">=3.6",
)
