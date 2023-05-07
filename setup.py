import os

from setuptools import find_packages, setup

with open("./requirements.txt") as text_file:
    requirements = text_file.readlines()

requirements = list(map(lambda x: x.rstrip("\n"), requirements))
install_libraries = [x for x in requirements if not x.startswith("--extra-index")]


def calculate_version():
    """Function to calculate the version based on
    the TAG exported in the environment variable from tags.sh
    """
    DEFAULT_VERSION = "v0.0.1"
    version = os.getenv("TAG") or DEFAULT_VERSION
    print("New Version Tag: ", version)

    if version.startswith("v"):
        return version[1:]
    else:
        return version


__version__ = calculate_version()


setup(
    name="pymob",
    version=__version__,
    description="Model based recursive partitioning implementation in python",
    author="Advance Analytics",
    author_email="sparsh.dtt@gmail.com",
    packages=find_packages(include=["pymob", "pymob.*"]),
    include_package_data=True,
    install_requires=install_libraries,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
