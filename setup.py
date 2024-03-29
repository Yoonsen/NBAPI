import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NBAPI",
    version="0.2",
    author="Lars G B Johnsen",
    author_email="yoonsen@gmail.com",
    description="API for National Library of Norway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yoonsen/Modules",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)