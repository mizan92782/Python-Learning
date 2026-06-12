
topic = "initial"


def func():
    '''to change a global variable in a scope we hav to exlplain is as global otherwise it consider as scope vaiable'''
    
    global topic 
    topic=topic +": in scope"
    print("topic value in scope: --------",topic)
    
   
print(f"Before calling the function : {topic}") 
func()
print(f"After calling the value,its scope change gloabal value: ---- {topic}")