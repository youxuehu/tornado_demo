# !/usr/bin/env python
# coding: UTF-8
# -*- coding:utf-8 -*-
import os
from setuptools import find_packages
from setuptools import setup

install_requires = []
exclude_file_patterns = [".git"]
version = {}
with open(os.path.join("tornado_demo/_version.py")) as fp:
    exec(fp.read(), version)
setup(
    name="tornado_demo",
    version=version["__version__"],
    description="tornado_demo",
    url="",
    author="tiger",
    install_requires=install_requires,
    packages=find_packages(where=".", exclude=exclude_file_patterns),
    package_data={"": ["*.so", "*.jar", "templates/**", "static/**/*"]},
    include_package_data=True,
    entry_points={"console_scripts": ["tornado_start=tornado_demo.__main__:main"]},
)
