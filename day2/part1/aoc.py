import time, psutil, os

def is_safe_report(nums):
    if len(nums) <= 1: return True
    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    return (not any(abs(d) > 3 or d == 0 for d in diffs) and
            (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)))

def process_file(filename):
    mem_start = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
    
    with open(filename) as f:
        safe = [nums for nums in ([int(x) for x in line.split()] for line in f) if is_safe_report(nums)]
    
    mem_end = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
    return len(safe), mem_end - mem_start

if __name__ == "__main__":
    t_start = time.time()
    result, mem_used = process_file('data.txt')
    
    print(f"Safe reports: {result}")
    print(f"Time: {time.time()-t_start:.4f}s")
    print(f"Memory: {mem_used:.2f}MB")