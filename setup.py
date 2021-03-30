import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = []
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setuptools.setup(
    name="ctrl4bi",
    version="1.0.4",
    author="Shaji James",
    author_email="shajijames7@gmail.com",
    description="A helper package for Business Intelligence solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vkreat-tech/ctrl4bi",
    include_package_data=True,
    packages=setuptools.find_packages(),
    package_data={
        "": ["*.txt", "*.gz", "*.csv"]
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)