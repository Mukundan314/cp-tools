from setuptools import setup

with open("README.rst", "r") as fd:
    long_description = fd.read()

setup(
    name="cp-tools",
    version="0.1.0",
    description="Competitive Programing Tools",
    long_description=long_description,
    author="Mukundan Senthil",
    author_email="mukundan314@gmail.com",
    url="https://github.com/Mukundan314/cp-tools",
    install_requires=["beautifulsoup4"],
    packages=["cp_tools"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    license="MIT",
)
