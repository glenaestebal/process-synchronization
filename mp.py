import threading
import time

# initialization of semaphores
mutex = 1
full_rooms = 0
empty_rooms = n # all rooms are empty at the start


# mga blue ang nagbibihis
def blues_nagbibihis(n, b):
    print("blues only")

# mga green ang nagbibihis
def greens_nagbibihis(n, g):
    print("greens only")


# array of two semaphores daw: door lock and dressing rooms lock
door_lock = Semaphore() # binary semaphore
dressing_rooms_lock = Semaphore() # counting semaphore

# input--------------------------------------------
n, b, g = list(map(int,input().strip().split(" ")))


# creating the threads
blue_thread = threading.Thread(target=blues_nagbibihis, args=(n, b))
green_thread = threading.Thread(target=greens_nagbibihis, args=(n, g))

# starting the threads
blue_thread.start()
green_thread.start()

# stopping the thread after completion of the task 
# (not sure kung saan siya kailangan in this problem or kung need ba)
blue_thread.join()
green_thread.join()


