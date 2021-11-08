#!/usr/bin/env python3
from os.path import dirname, join
import setuptools
# import PYSlots.__init__ as __init__

setuptools.setup(
    name="PYSlots",
    version="1.0.698",
    author="Lukas-Batema",
    author_email="lukasbatema@gmail.com",
    description="A fun terminal Python slots game!",
    long_description=open(join(dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Lukas-Batema/pyslots",
    project_urls={
        "Bug Tracker": "https://github.com/Lukas-Batema/pyslots/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["PYSlots"],
    install_requires=["wheel", "setuptools"],
    keywords=["slots", "python", "py"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pyslots=PYSlots.__main__:main",
        ]
    },
)
