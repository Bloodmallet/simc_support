from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='simc_support',
    version='9.0.0.0',
    author='Bloodmallet(EU)',
    author_email='kruse.peter.1990@gmail.com',
    description='This package offers some World of Warcraft related ingame data regularly used for simulations and some basic input test for standard values of SimulationCraft.',
    long_description=readme(),
    url='https://github.com/Bloodmallet/simc_support',
    packages=[
        'simc_support',
    ],
    package_data={
        "": ["*.md",],
    },
    python_requires='>=3.6',
    license='GNU GENERAL PUBLIC LICENSE',
)
