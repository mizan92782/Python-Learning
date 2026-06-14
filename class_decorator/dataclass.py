
from dataclasses import dataclass

#------------------ user as struct
'''
reduce boilerplate code
automatically generate:
__init__
__repr__
__eq__
'''
@dataclass
class Student:
    name: str
    age: int