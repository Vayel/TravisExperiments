from setuptools import setup

import package



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
    license="MIT"
)
