from setuptools import find_packages, setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="simc_support",
    author="Bloodmallet(EU)",
    author_email="bloodmalleteu@gmail.com",
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
    version_config={
        "template": "{tag}",
        "dev_template": "{tag}+{branch}.{ccount}.{sha}",
        "dirty_template": "{tag}+{branch}.{ccount}.{sha}.dirty",
        # schema: <wow_version, e.g. 9.0.1>.<own_version_per_wow_version>
        "starting_version": "0.0.0.1",
        "version_callback": None,
        "version_file": None,
        "count_commits_from_version_file": False,
        "branch_formatter": None,
    },
    setup_requires=["setuptools-git-versioning"],
)
