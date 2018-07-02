import io
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with io.open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_DEPS = ['faker>0.8.0']
MONGO_DEPS = ['pymongo']
TEST_DEPS = ['pytest'] + MONGO_DEPS
DEV_DEPS = MONGO_DEPS

setup(
    name="fake-gen",
    # https://pypi.python.org/pypi/setuptools_scm
    use_scm_version=True,

    author="Arie Bro",
    author_email="ariebro@gmail.com",
    maintainer="Pau Ruiz Safont",
    maintainer_email="psafont@ebi.ac.uk",
    description="A small package that helps generate content to fill databases for tests",
    url="http://github.com/psafont/fake-gen",
    license="MIT",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=[
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
        'Programming Language :: Python :: 3.7',
    ],
    keywords="factory testing test unittest mongo data generator database json elasticsearch",

    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,

    install_requires=INSTALL_DEPS,
    setup_requires=[
        'setuptools_scm'
    ],
    extras_require={
        'dev': DEV_DEPS,
        'test': TEST_DEPS,
        'mongo': MONGO_DEPS
    },
)
