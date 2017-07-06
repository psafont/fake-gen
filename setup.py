import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version():
    VERSION = fread("VERSION").strip()
    build_number = os.environ.get('BUILD_NUMBER', None)
    if build_number:
        return VERSION + "b{}".format(build_number)
    return VERSION

setup(
    name = "python-testdata",
    version = get_version(),
    author = "Arie Bro",
    author_email = "ariebro@gmail.com",
    description = "A small package that helps generate content to fill databases for tests.",
    url = "http://github.com/arieb/python-testdata",
    license = "MIT",
    long_description=fread('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords = "factory testing test unittest mongo data testdata database json elasticsearch",

    packages = find_packages(exclude=['docs', 'tests']),
    include_package_data=True,

    install_requires = [
        'faker == 0.7.17'
    ],
        extras_require={
        'test': ['pytest'],
        },
)
