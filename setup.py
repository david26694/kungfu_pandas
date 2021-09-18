from setuptools import setup, find_packages

requirements = ['pandas']

setup(
    name="kungfu_pandas",
    version="0.1.0",
    packages=find_packages(),
    requires=requirements,
    install_requires=requirements,
    setup_requires=requirements,
)
