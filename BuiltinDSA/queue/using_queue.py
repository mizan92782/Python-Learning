from queue import Queue

# Queue assing
num=Queue()
print("initial size ",num.qsize())


# push in queue
num.put(44)
num.put(23)
num.put(32)
num.put(88)
num.put(212)


# pop from queue
num.get()


while not num.empty():
    print(num.get())
    

    
while not num.empty():
    print(num.get())