import threading
import time


# mga blue ang nagbibihis
def blues_nagbibihis(n, b, id):
    print("blues only")

# mga green ang nagbibihis
def greens_nagbibihis(n, g,id):
    if green_count+1 < n: # as long as number of green threads inside the dressing is less than n
        green_count+= 1

        #print appropriate string
        if green_count == 0: #first to enter
            print("greens only")
        else:
            print("Green thread: ", id, " has entered.")

        #dont allow blues

        #green threads will wait 1 second inside the fitting before exit
        door_lock.release()
        green_count -= 1

        if green_count == 0:
            print("Empty fitting room")
    else: #dont allow any threads inside
        print("Dressing room is full rn")



# input--------------------------------------------
n, b, g = list(map(int,input().strip().split(" ")))

# initialization of semaphores
mutex = 1 #idk what this is for :<
full_rooms = 0
empty_rooms = n # all rooms are empty at the start
blue_count = 0 #counts how many threads inside a room
green_count = 0 #counts how many threads inside a room

# array of two semaphores daw: door lock and dressing rooms lock
door_lock = Semaphore() # binary semaphore -- for color, makes sure blue cant enter when green is inside
dressing_rooms_lock = Semaphore(n) # counting semaphore ; tracks how many threads per room and how many have accessed it 


# creating the threads
for x in range(b):
    blue_thread = threading.Thread(target=blues_nagbibihis, args=(n, b, x))
    blue_thread.start()

for x in range(g):
    green_thread = threading.Thread(target=greens_nagbibihis, args=(n, g,x))
    green_thread.start()

# starting the threads
# blue_thread.start()
# green_thread.start()

# stopping the thread after completion of the task 
# (not sure kung saan siya kailangan in this problem or kung need ba)
blue_thread.join()
green_thread.join()


