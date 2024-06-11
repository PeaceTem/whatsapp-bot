import timeit

def test():
    print("Hello, world!")



# Measure the execution time of example_function
execution_time = timeit.timeit("test()", setup="from __main__ import test", number=30)
print("Doing the timing job")
print(f"Execution time: {execution_time / 30} seconds per call")