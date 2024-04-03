import os
from setuptools import setup, find_packages
import sys

sys.path.append(os.path.dirname(__file__))

import confpass

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

pkgs = find_packages(exclude=('examples', 'docs', 'resources', 'user_guide'))

setup(
    name='confpass',
    description='CONFPASS',
    long_description=readme,
    long_description_content_type='text/markdown',
    license=license,
    packages=pkgs,
    install_requires=install_requires,
)