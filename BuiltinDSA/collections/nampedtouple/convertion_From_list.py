

#========= We can convert a list to nampetouple



import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])



li = ['Manjeet', '19', '411997']

# list to nameptoupe
S = Student._make(li)


print(S)
