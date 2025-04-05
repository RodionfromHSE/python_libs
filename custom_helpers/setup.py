from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="custom_helpers",  # The package name users will use to install
    version="0.1.0",
    packages=find_packages(where="src"),  # Look for packages in the "src" folder
    package_dir={"": "src"},  # Map root of the package to "src"
    python_requires=">=3.10",
    install_requires=[
        "omegaconf"
    ],
    description="A set of helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rodion Khvorostov",
    author_email="rodion.khvorostov@jetbrains.com",
)
