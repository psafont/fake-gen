from setuptools import setup, find_packages
from codecs import open
from os import path

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def get_contents(filename):
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, filename), encoding='utf-8') as f:
        contents = f.read()
    return contents


setup(
    name = "python-testdata-tsi",
    # https://pypi.python.org/pypi/setuptools_scm
    use_scm_version = True,

    author = "Arie Bro",
    author_email = "ariebro@gmail.com",
    maintainer = "Pau Ruiz Safont",
    maintainer_email = "psafont@ebi.ac.uk",
    description = "A small package that helps generate content to fill databases for tests.",
    url = "http://github.com/psafont/python-testdata",
    license = "MIT",
    long_description = get_contents('README.md'),
    classifiers = [
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords = "factory testing test unittest mongo data testdata database json elasticsearch",

    packages = find_packages(exclude=['docs', 'tests']),
    include_package_data = True,

    install_requires = [
        'fake-factory == 0.3.2'
    ],
    setup_requires = [
        'setuptools_scm'
    ],
    extras_require = {
        'test': ['pytest', 'pymongo'],
        'mongo': ['pymongo']
    },
)
