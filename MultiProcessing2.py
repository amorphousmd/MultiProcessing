import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done sleeping after {seconds}'


# 10 processes at the same time
processes = []

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # A future object encapsulate the execution of out functions and allows us to check on it after it's done
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]  # List comprehension

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} seconds')
