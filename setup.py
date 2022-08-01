# This file is part of packager
# Copyright (C) 2022 - Mattia G. Bergomi

import sys
from setuptools import find_packages, setup

CURRENT_PYTHON_VERSION = sys.version_info[:2]
MIN_REQUIRED_PYTHON_VERSION = (3, 7) # COMPATIBLE PYTHON VERSION
if CURRENT_PYTHON_VERSION < MIN_REQUIRED_PYTHON_VERSION:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of py_repo_structure requires Python {}.{}, but you're trying to
install it on Python {}.{}.
""".format(*(MIN_REQUIRED_PYTHON_VERSION + CURRENT_PYTHON_VERSION)))
    sys.exit(1)

requirements = [
    'docopt'
] 
EXCLUDE_FROM_PACKAGES = []

setup(
    name='packager',
    version='0.1.0',
    python_requires='>={}.{}'.format(*MIN_REQUIRED_PYTHON_VERSION),
    url='',
    author='',
    author_email='',
    description=(''),
    license='',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'py_packager = packager.create_structure:main',
            ],
        },
    zip_safe=False,
)
