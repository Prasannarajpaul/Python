## processes that run in parallel
## When to use?
### CPU-Bound tasks that are heavy on CPU usage (e.g., mathematical computations, data processing)
### Parallel execution in such a way i use all the cores in the cpu. Multiple cores of the CPU

import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_num():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":

    # create 2 process
    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)
    t =time.time()

    ## Start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(f"Time: {finished_time}")

