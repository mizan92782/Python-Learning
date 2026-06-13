

from functools import reduce

a = ['mizan','is' ,'good','boy']

messageg = reduce(lambda x,y: x+" "+y,a)
print(messageg)





#======================= accumulative /summetiaon

num =[4,5,2,5,22,44,33]
sum = reduce(lambda x,y : x+y,num)
print(sum)



#============= greeter number
greater = reduce(lambda x,y : x if x>y else y,num)
print(greater)
