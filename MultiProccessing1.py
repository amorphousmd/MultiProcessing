import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done sleeping...')


# 10 processes at the same time
processes = []

if __name__ == '__main__':
    for _ in range(10):  # The _ is just a throw away variable meaning we don't need to use the integer
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)
        # We can't use .join() here because it will finish the process before looping, which is just like
        # running the script asynchronously

    # Start all the process and make another loop to join all the processes
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} seconds')
