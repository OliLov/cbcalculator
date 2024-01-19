"""Setup for PyCBCount."""
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

DESC = "A Python package for calculating Complete Blood Count (CBC) metrics"

setup(
    name="pycbcount",
    version="0.0.1",
    description=DESC,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OliLov/pycbcount",
    author="Oliver Lövström",
    author_email="oliver.lovstrom@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
