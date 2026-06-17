import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

H=Student('Himesh','19','26082003')
# .__getnewargs__ returns the named tuple as a plain tuple
print(H.__getnewargs__())