import threading
import time
import queue


# initialization of semaphores
mutex = 1 #idk what this is for :<
full_rooms = 0
blue_count = 0 #counts how many threads inside a room
green_count = 0 #counts how many threads inside a room
color = ''
q = []




# mga blue ang nagbibihis
def blues_nagbibihis( n, b, id):
    global blue_count
    global color  
    global q  
    if dressing_rooms_lock.acquire(blocking=False) and green_lock.acquire(blocking = False) :
                green_lock.release()
                
        # if blue_count + 1 < n:
            # if color == 'b' or color == '':
                blue_count+= 1
                #print appropriate string
                if blue_count == 1: #first to enter
                    print("Blue only")
                    #dont allow greens
                    # door_lock.acquire()
                    blue_lock.acquire()
                    color = 'b'
                    print("Blue thread: ", id, " has entered.")
                else:
                    print("Blue thread: ", id, " has entered.")

                # Log how many threads are in the dressing room
                # dressing_rooms_lock.acquire()

                
                #green threads will wait 2 seconds inside the fitting before exit
                time.sleep(2)

                #Exit blue lock
                print("Blue thread: ", id," exits.") 
                dressing_rooms_lock.release()
                blue_count -= 1

                #If dressing room is empty
                if (blue_count == 0): 
                    color = ''
                    print("Dressing room is empty. Blue") 
                    blue_lock.release()
            
    else: #dont allow any threads inside, idk what the threads do while waiting
        # print("Dressing room is full rn. BLue") 
        q.append(['B',id])

# mga green ang nagbibihis
def greens_nagbibihis(n, g, id):
    global green_count
    global color   
    global q 
    if dressing_rooms_lock.acquire(blocking=False) and blue_lock.acquire(blocking = False):

                blue_lock.release()
        # if green_count + 1 < n:
        #     if color == 'g' or color == '':
                green_count+= 1
                # Log how many threads are in the dressing room
                # dressing_rooms_lock.acquire()

                #print appropriate string
                if green_count == 1: #first to enter
                    print("Green only")
                    #dont allow blues
                    # door_lock.acquire()
                    green_lock.acquire()
                    color = 'g'
                    print("Green thread: ", id, " has entered.")
                else:
                    print("Green thread: ", id, " has entered.")


                
                #green threads will wait 1 seconds inside the fitting before exit
                time.sleep(1)

                #Exit green lock
                print("Green thread: ", id," exits.") 
                dressing_rooms_lock.release()
                green_count -= 1

                #If dressing room is empty
                if (green_count == 0):  
                    color = ''
                    print("Dressing room is empty. Green") 
                    green_lock.release()
            
    else: #dont allow any threads inside, idk what the threads do while waiting
        # print("Dressing room is full rn. Green") 
        q.append(['G',id])



# input--------------------------------------------
n, b, g = list(map(int,input().strip().split(" ")))

# array of two semaphores daw: door lock and dressing rooms lock
green_lock = threading.Semaphore(1) # binary semaphore -- for color, makes sure blue cant enter when green is inside
blue_lock = threading.Semaphore(1) # binary semaphore -- for color, makes sure blue cant enter when green is inside

dressing_rooms_lock = threading.Semaphore(n) # counting semaphore ; tracks how many threads per room and how many have accessed it 


for i in range(int(b)):
    q.append(['B',i])

for i in range(int(g)):
    q.append(['G',i])


while len(q) > 1:
    if q[0][0] == 'B':
        thread_1 = threading.Thread(target = blues_nagbibihis, args = (n,b,q[0][1]))
        thread_1.start()
        q.pop(0)
    if q[0][0] == 'G':
        thread_1 = threading.Thread(target = greens_nagbibihis, args = (n,g,q[0][1]))
        thread_1.start()
        q.pop(0)

 
