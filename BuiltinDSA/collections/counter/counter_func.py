from collections import Counter
ctr = Counter([1, 2, 2, 3, 3, 3])

print("Counter: ", ctr)




#======== Update counter ==========
ctr.update([4,3,5,2])
print("Counter: ", ctr)



# extract
num = list(ctr.elements())
print("extracted element : ", num)




print("most frequency element: ",ctr.most_common(1))
print("most frequency element: ",ctr.most_common(5))


# increase counter manually :
ctr[3]+=8
ctr[4] += 5
print("counter after manually increae : ",ctr)


# subtract
ctr.subtract([2, 2, 3])
print(ctr)






a
#Arithmatic operatios...........
from collections import Counter
ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])

print(ctr1 + ctr2)   # Addition
print(ctr1 - ctr2)   # Subtraction 
print(ctr1 & ctr2)   # Intersection
print(ctr1 | ctr2)   # Union