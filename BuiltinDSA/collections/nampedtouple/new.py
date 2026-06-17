import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Student.__new__ returns a new instance of Student(name,age,DOB)
print(Student.__new__(Student,'Himesh','19','26082003'))