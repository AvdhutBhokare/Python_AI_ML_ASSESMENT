"""
Scenario 2: Logging Decorator
Task: Create a decorator @log_execution_time that logs the time taken to execute a function. 
Use it to log the runtime of a sample function calculate_sum(n) that returns the sum of numbers from 1 to n.
"""

import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute")
        return result
    return wrapper


@log_execution_time
def calculate_sum(n):
    total = sum(range(1, n + 1))
    return total


# Function call
result = calculate_sum(1000000)

# Output
print(f"Sum: {result}")
