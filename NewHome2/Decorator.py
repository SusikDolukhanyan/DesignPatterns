import time


def simple_function():
    print("Executing the main function.")

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed successfully.")
        return result
    return wrapper


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds.")
        return result
    return wrapper


@log_decorator
@time_decorator
def complex_function():
    print("Performing some complex calculations...")
    time.sleep(1)
    print("Calculations done!")


complex_function()
