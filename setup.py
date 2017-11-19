"""A setuptools based setup module for the PewDiePlot library."""

from setuptools import setup, find_packages

NAME = 'pewdieplot'

requirements = list(open('requirements.txt', 'r').readlines())
test_requirements = requirements
extras_require = {}

setup(
    name=NAME,
    version='0.1',
    description="High-level API for Pyplot to easily create beautiful graphs.",
    long_description='',
    url='https://github.com/flosch/pewdieplot',
    author='Florian Schäfer',
    author_email='florian.joh.schaefer@gmail.com',
    license='MIT',
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=requirements,
    tests_require=test_requirements,
    extras_require=extras_require,
    zip_safe=False,
    test_suite='tests'
)
