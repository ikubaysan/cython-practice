from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name='cython_practice',
    packages=find_packages(),
    ext_modules=cythonize("modules/*.pyx"),
)
# 