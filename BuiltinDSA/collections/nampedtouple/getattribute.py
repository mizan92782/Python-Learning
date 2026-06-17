# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')



#=========== besige index and name ,we also can acces by getattr funct

print(getattr(S,'DOB'))