#!/usr/bin/env python
"""Bag setup."""

import os
from setuptools import setup

setup(
    name="bag",
    version="1.3.1",
    description="McGill Robotics ROS Bagger",
    author="McGill Robotics",
    author_email="dev@mcgillrobotics.com",
    license="MIT",
    url="https://github.com/mcgill-robotics/compsys",
    packages=["bag", "bag.cmd", "bag.util"],
    entry_points={"console_scripts": ["bag = bag.__main__:main"]},
    zip_safe=True,
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
    ])
