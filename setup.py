
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
from os.path import join, dirname

import exness


setup(
    name="exness_crawler",
    version=exness.__version__,
    description="Exness crawler",
    author="Alexander Ruzhnikov",
    author_email="ruzhnikov85@gmail.com",
    python_requires='>=3',
    install_requires=['feedparser'],
    packages=find_packages(exclude=['tests']),
    long_description="""
        Crawler for colleting and manipulate data
        from many type of resources(Rss, Atom, etc)
        """
)
