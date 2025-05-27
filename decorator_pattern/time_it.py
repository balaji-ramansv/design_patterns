import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Task started at {start_time}")
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Task ended at {end_time}")
        print(f"Time taken: {end_time - start_time}")

    return wrapper

@time_it
def perform_something():
    print("doing something")
    time.sleep(2)
    print("done")


perform_something()
