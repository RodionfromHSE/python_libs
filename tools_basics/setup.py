from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
long_description = (Path(__file__).parent / "README.md").read_text()


setup(
    name="tools_basics",  # The package name users will use to install
    version="0.1.0",
    packages=find_packages(where="src"),  # Look for packages in the "src" folder
    package_dir={"": "src"},  # Map root of the package to "src"
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "datasets",
        "omegaconf",
        "tabulate",
        "bokeh"
    ],
    python_requires=">=3.10",
    description="A set of tools for the lesson on basics (LLM Course)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rodion Khvorostov",
    author_email="rodion.khvorostov@jetbrains.com",
)
