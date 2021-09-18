from setuptools import setup, find_packages

requirements = ['pandas']

test_requirements = ['pytest'] + requirements
dev_requirements = test_requirements + ['pre-commmit']

setup(
    name="kungfu_pandas",
    version="0.1.1",
    packages=find_packages(),
    requires=requirements,
    install_requires=requirements,
    setup_requires=requirements,
    extras_require={'dev': dev_requirements, 'test': test_requirements},
)
