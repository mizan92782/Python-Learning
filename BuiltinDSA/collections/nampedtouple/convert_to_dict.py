#========== we can conver a namedtoupe to a dictions



import collections
# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

#============ conver to dict
dic = S._asdict()

print(dic)