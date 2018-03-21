from setuptools import setup, find_packages
from codecs import open
from os import path

VERSION = '0.0.0'

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

PACKAGES = find_packages(exclude=['docs', 'tests'])

# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name='mypackage',
    version=VERSION,
    description='A sample Python project',
    long_description=long_description,
    url='https://github.com/oyamad/MyPackage',
    author='Daisuke Oyama',
    author_email='oyama@e.u-tokyo.ac.jp',
    license='BSD',
    classifiers=CLASSIFIERS,
    keywords=['sample'],
    packages=PACKAGES,
    install_requires=[
        'numpy', 'scipy', 'numba'
    ],
    extras_require={
        'test': ['nose'],
    },
)
