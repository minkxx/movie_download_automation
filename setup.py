# version 0.1.0

from setuptools import setup, find_packages

setup(
    name='movie_ls',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.13.4',
        'selenium==4.34.2'
    ],
)