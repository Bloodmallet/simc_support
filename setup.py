from setuptools import setup

setup(
    version_config={
        "template": "{tag}",
        "dev_template": "{tag}.dev1+{branch}.{ccount}.{sha}",
        "dirty_template": "{tag}.dev1+{branch}.{ccount}.{sha}.dirty",
        # schema: <wow_version, e.g. 9.0.1>.<own_version_per_wow_version>
        "starting_version": "0.0.0.1",
        "version_callback": None,
        "version_file": None,
        "count_commits_from_version_file": False,
        "branch_formatter": None,
    },
)
