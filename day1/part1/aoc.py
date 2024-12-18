import time, psutil, os
from typing import List, Tuple

def measure_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        initial_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
        result = func(*args, **kwargs)
        exec_time = time.time() - start_time
        mem_used = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 - initial_mem
        print(f"Report: {result}\nTime: {exec_time:.4f}s\nMemory: {mem_used:.2f}MB")
    return wrapper

@measure_performance
def solve_distance(file_path: str = 'data.txt') -> int:
    with open(file_path) as f:
        left, right = zip(*(map(int, line.split()) for line in f if line.strip()))
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))

if __name__ == "__main__":
    solve_distance()