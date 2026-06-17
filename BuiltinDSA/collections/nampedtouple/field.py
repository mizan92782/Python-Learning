import collections
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(S._fields)