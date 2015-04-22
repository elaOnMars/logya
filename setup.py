#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from logya import __version__


readme = open('README.rst').read()
license = open('LICENSE').read()
requirements = open('requirements.txt').read().splitlines()

setup(
    name='logya',
    version=__version__,
    description='Logya: easy to use and flexible static Web site generator.',
    long_description=readme,
    url='https://pythonhosted.org/logya/',
    author='Ramiro Gómez',
    author_email='code@ramiro.org',
    maintainer='Ramiro Gómez',
    maintainer_email='code@ramiro.org',
    keywords=['Website Generator'],
    license=license,
    packages=['logya'],
    include_package_data=True,
    exclude_package_data={'': ['*.pyc']},
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Site Management'],
    entry_points={
        'console_scripts': [
            'logya = logya.main:main'
        ]
    },
    test_suite='tests',
    tests_require=['tox', 'mock'],
)
