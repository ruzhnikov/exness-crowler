
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

import resources_crawler


setup(
    name="resources_crawler",
    version=resources_crawler.__version__,
    description="Collector of resources",
    author="Alexander Ruzhnikov",
    author_email="ruzhnikov85@gmail.com",
    python_requires='>=3',
    tests_require=["pytest"],
    install_requires=['feedparser'],
    packages=find_packages(exclude=['tests']),
    long_description="""
        Crawler for colleting and manipulate data
        from many type of resources(Rss, Atom, etc)
        """
)
