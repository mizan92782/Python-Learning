
'''ython-এ “Pass by Value” আর “Pass by Reference” নিয়ে অনেকেরই কনফিউশন থাকে। আসলে Python একদম C/C++ এর মতো strict pass-by-value বা pass-by-reference ব্যবহার করে না। Python ব্যবহার করে:

Pass by Object Reference (বা Call by Assignment)

কিন্তু সহজভাবে বোঝার জন্য আমরা এটাকে ২ ভাগে বুঝতে পারি:

Mutable object behavior (list, dict)
Immutable object behavior (int, str, tuple)'''


#============ passed by reference ==============

def myFun(x):
    x[0] = 20
    print(f"Memory of {x} (object) :(object) {id(x)}")

b = [10, 11, 12, 13]
print(f"Memory of {b} (object) :(object) {id(b)}")
myFun(b)
print(b)

#=================== here both hava some memroy addres as its passed by refernce


#============== passed by balue
def myFun2(x):
    
    # 50  is another object
    x = x+40
    print(x)
    print(f"Memory of {x} (object) :(object) {id(x)}")
    
    
# here 10 is a object that refer to varibale x
x = 10
print(f"Memory of {x} (object): {id(x)}")
myFun2(x)
print(x)

# memory oddress of object of x in not same in function and out of function
# its is passed only value