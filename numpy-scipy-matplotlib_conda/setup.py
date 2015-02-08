import os
import sys

from setuptools import setup

import package

# Requirements
def strip_comments(l):
    return l.split("#", 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(os.path.join(os.getcwd(), *f)).readlines()]))
    
requirements = reqs("requirements.txt")


setup(
    name="package",
    version="0.0.1",
    description="",
    long_description="",
    author="Vayel",
    author_email="vincent.lefoulon@free.fr",
    url="https://github.com/Vayel/TravisExperiments",
    packages=["package"],
    package_dir={"package": "package"},
    include_package_data=True,
    install_requires=requirements,
    license="MIT"
)
