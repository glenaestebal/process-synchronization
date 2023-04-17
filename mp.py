import threading
import time


# initialization of semaphores
mutex = 1 #idk what this is for :<
full_rooms = 0
blue_count = 0 #counts how many threads inside a room
green_count = 0 #counts how many threads inside a room



# mga blue ang nagbibihis
def blues_nagbibihis(n, b, id):
    global blue_count
        
    if blue_count +1  <= n: # as long as number of green threads inside the dressing is less than n
        blue_count+= 1

        #print appropriate string
        if blue_count == 1: #first to enter
            print("Blue only")
            #dont allow blues
            door_lock.acquire()
            print("Blue thread: ", id, " has entered.")
        else:
            print("Blue thread: ", id, " has entered.")

        # Log how many threads are in the dressing room
        dressing_rooms_lock.acquire()

        
        #green threads will wait 2 seconds inside the fitting before exit
        time.sleep(2)

        #Exit blue lock
        print("Blue thread: ", id," exits.") 
        dressing_rooms_lock.release()
        blue_count -= 1

        #If dressing room is empty
        if (blue_count == 0): 
            print("Dressing room is empty. Blue") 
            door_lock.release()
        
    else: #dont allow any threads inside, idk what the threads do while waiting
        print("Dressing room is full rn. BLue") 

# mga green ang nagbibihis
def greens_nagbibihis(n, g, id):
    global green_count
        
    if green_count +1  <= n: # as long as number of green threads inside the dressing is less than n
        green_count+= 1

        #print appropriate string
        if green_count == 1: #first to enter
            print("Green only")
            #dont allow blues
            door_lock.acquire()
            print("Green thread: ", id, " has entered.")
        else:
            print("Green thread: ", id, " has entered.")

        # Log how many threads are in the dressing room
        dressing_rooms_lock.acquire()

        
        #green threads will wait 2 seconds inside the fitting before exit
        time.sleep(2)

        #Exit green lock
        print("Green thread: ", id," exits.") 
        dressing_rooms_lock.release()
        green_count -= 1

        #If dressing room is empty
        if (green_count == 0):  
            print("Dressing room is empty. Green") 
            door_lock.release()
        
    else: #dont allow any threads inside, idk what the threads do while waiting
        print("Dressing room is full rn. Green") 



# input--------------------------------------------
n, b, g = list(map(int,input().strip().split(" ")))
empty_rooms = n # all rooms are empty at the start

# array of two semaphores daw: door lock and dressing rooms lock
door_lock = threading.Semaphore(1) # binary semaphore -- for color, makes sure blue cant enter when green is inside
dressing_rooms_lock = threading.Semaphore(n) # counting semaphore ; tracks how many threads per room and how many have accessed it 

for x in range(g):
    green_thread = threading.Thread(target=greens_nagbibihis, args=(n, g,x))   
    green_thread.start()
# creating the threads
for x in range(b):
    blue_thread = threading.Thread(target=blues_nagbibihis, args=(n, b, x))
    blue_thread.start()

    


# starting the threads
# blue_thread.start()
# green_thread.start()

# stopping the thread after completion of the task 
# (not sure kung saan siya kailangan in this problem or kung need ba)
blue_thread.join()
green_thread.join()


