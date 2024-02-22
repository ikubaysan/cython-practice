# Python version of the sum_list function
def sum_list_py(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# Cython version of the sum_list function
def sum_list_cy(numbers):
    cdef int total = 0
    cdef int n
    for n in numbers:
        total += n
    return total