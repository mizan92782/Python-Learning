import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', 
                           ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# ._replace returns a new namedtuple, 
# it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='Manjeet'))