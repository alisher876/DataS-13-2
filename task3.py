import time

def decorator_1(func):
    def wrapper(*a, **b):
        start_time = time.time()
        result = func(*a, **b)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper
