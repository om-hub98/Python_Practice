
### Synchronous vs Asynchronous Functions

#Sync Functions: 
# In synchronous programming, tasks are executed one after the other. 
# Each task must complete before the next one starts. 
# This can lead to delays if a task takes a long time to finish.

'''
import time

def task1():
    print("Task 1")
    time.sleep(3)

def task2():
    print("Task 2")
    time.sleep(3)

print("Starting tasks...")
start_time = time.time()
task1()
task2()
end_time = time.time()
print("All tasks completed.")
print(f"Total time taken: {end_time - start_time} seconds.")

'''


# Async Functions: 
# In asynchronous programming, tasks can be executed concurrently. 
# This means that while one task is waiting (for example, for I/O operations), 
# other tasks can continue to run. 
# This can lead to better performance and responsiveness in applications.


import asyncio
import time

async def task1():
    print("Task 1")
    await asyncio.sleep(3)

async def task2():
    print("Task 2")
    await asyncio.sleep(3)

async def main():
    start_time = time.time()
    await asyncio.gather(task1(), task2())
    end_time = time.time()
    
    print(f"Total time taken: {end_time - start_time} seconds.")

print("Starting tasks...")
asyncio.run(main())
print("All tasks completed.")