from concurrent.futures import ThreadPoolExecutor

def function_one(a, b):
    return f"Result from function one {a} {b}"

def function_two():
    return "Result from function two"

def function_three():
    return "Result from function three"

# Use ThreadPoolExecutor to run functions concurrently
with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(function_one, 1, 2),
        executor.submit(function_two),
        executor.submit(function_three)
    ]

# Collect results
results = [future.result() for future in futures]

# Print the results
print("Results from all functions:")
for result in results:
    print(result)