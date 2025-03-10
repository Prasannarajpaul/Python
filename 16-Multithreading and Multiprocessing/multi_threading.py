    #### Multithreading
## When to use Multi Threading
### I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests)
### Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)# made sleep as it will has I/O operation
        print(f"Number: {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

# t=time.time()
# print_numbers()
# print_letter()
# finished_time = time.time()-t
# print(finished_time) #20 seconds

# Creating 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()
# start the thread
t1.start()
t2.start()

## Wait for the threads to complete
t1.join()
t2.join() # need to make into one thread so that remaining code to work

finished_time = time.time() - t
print(finished_time) #10 seconds
