import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covidSumm",
    version="0.1.3",
    author="SU Dan",
    author_email="sudan0317@gmail.com",
    description="summerization for CORD-19.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Iamfinethanksu/covid_summarization",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'easydict'
    ],
    python_requires='>=3.6',
)
