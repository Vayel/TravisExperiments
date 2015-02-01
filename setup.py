import os
import sys
from setuptools import setup, find_packages

import package



def strip_comments(l):
    return l.split('#', 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(os.path.join(os.getcwd(), *f)).readlines()]))


install_requires = reqs("requirements.txt")

packages = ["package"]

classifiers = [
    "Programming Language :: Python"
]

setup(
    name="package",
    packages=packages,
    author="Vayel",
    description="",
    long_description="",
    license="GPL",
    classifiers=classifiers,
    install_requires=install_requires,
    include_package_data=True
)
