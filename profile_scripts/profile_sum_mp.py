import multiprocessing
import time
from modules.sum_list import sum_list_py, sum_list_cy

def profile_function(func, numbers, n_processes):
    start_time = time.time()
    with multiprocessing.Pool(processes=n_processes) as pool:
        for _ in range(100):  # Adjust based on how many times you want to run
            pool.apply(func, args=(numbers,))
    end_time = time.time()
    print(f"{func.__name__} with {n_processes} processes took {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    numbers = list(range(1000000))
    for n_processes in [1, 2, 4]:
        profile_function(sum_list_py, numbers, n_processes)
        profile_function(sum_list_cy, numbers, n_processes)
