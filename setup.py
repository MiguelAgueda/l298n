import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="l298n",
    version="0.0.1",
    author="Psuedohim",
    author_email="8im8yhq1zatd@opayq.com",
    description="A module to assist in controlling an L298N H-Bridge motor driver.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Psuedohim/l298n",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
