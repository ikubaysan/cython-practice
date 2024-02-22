import timeit
import os

cwd = os.getcwd()
print(f"Current working directory: {cwd}")

from modules.sum_list import sum_list_cy, sum_list_py

# Create a large list of numbers
numbers = list(range(1000000))

# Time the Python version
py_time = timeit.timeit(lambda: sum_list_py(numbers), number=100)
print(f"Python version took {py_time:.4f} seconds")

# Time the Cython version
cy_time = timeit.timeit(lambda: sum_list_cy(numbers), number=100)
print(f"Cython version took {cy_time:.4f} seconds")
