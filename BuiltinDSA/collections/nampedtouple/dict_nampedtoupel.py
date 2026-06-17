import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])



#========== dictionary=========

di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

#========== convert to numpetouple

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))