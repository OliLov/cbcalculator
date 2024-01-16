"""Setup Configuration for CBCalculator."""
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

DESC = "A Python package for calculating Complete Blood Count (CBC) metrics"

setup(
    name="CBCalculator",
    version="0.0.1",
    packages=find_packages(),
    description=DESC,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Oliver Lövström",
    author_email="oliver.lovstrom@gmail.com",
    url="https://github.com/OliLov/CBCalculator",
    classifiers=[
        # Choose classifiers from https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
