from setuptools import setup
from setuptools import find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="simc_support",
    version="9.0.0.0",
    author="Bloodmallet(EU)",
    author_email="kruse.peter.1990@gmail.com",
    description="Data to support simulations for World of Warcraft with SimulationCraft.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Bloodmallet/simc_support",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_data={
        "": [
            "*.md",
        ],
        "simc_support": [
            "game_data/data_files/*.json",
        ],
    },
    python_requires=">=3.6",
    license="GNU GENERAL PUBLIC LICENSE",
)
