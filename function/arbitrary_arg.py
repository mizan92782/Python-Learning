def func(*args, **kwargs):
    
    print("args argument : ------- > \n")
    for arg in args:
        print(arg)
        
        
        
    print("kwargs argument : ---------> ")
    for key,value in kwargs.items():
        print(f"{key}   {value}")
        
    
        

func("one","two","three",four="four",five="five",six="six")