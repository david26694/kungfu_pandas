from setuptools import find_packages, setup

requirements = ['pandas']

test_requirements = ['pytest'] + requirements
dev_requirements = test_requirements + [
    'pre-commit', 'twine'
]

docs_requirements = [
    'mkdocs==1.1',
    'mkdocs-material==4.6.3',
    'mkdocstrings==0.8.0'
]

setup(
    name="kungfu_pandas",
    version="0.1.4",
    packages=find_packages(),
    requires=requirements,
    install_requires=requirements,
    setup_requires=requirements,
    extras_require={
        'dev': dev_requirements,
        'test': test_requirements,
        'docs': docs_requirements,
    },
)
