from setuptools import find_packages, setup
from fake_project import __version__

setup(
    name='fake_project',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version=__version__,
    description='fake demo project',
    author=''
)
