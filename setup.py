# Run with: python setup.py build_ext --inplace
from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name='cython_practice',
    packages=find_packages(),
    ext_modules=cythonize("modules/*.pyx", "sample_modules/*.pyx")

    ## Use the recursive glob pattern '**/*.pyx' to match all .pyx files in the directory and subdirectories
    #ext_modules=cythonize("modules/**/*.pyx", recursive=True),
)
