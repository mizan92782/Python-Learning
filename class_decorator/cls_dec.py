
class Calculation:
    clsmem="clss member"
    
    def __init__(self,radius):
        self._radius=radius
    
    @staticmethod
    def staticmeth():
        print("Static method no receive either self or clss")
    
    @classmethod
    def clsmethod(cls):
        cls.clsmethod="change member"
    
    @property
    def redius(self):
        print("access protected data,access like a variable")
    
        
    @redius.setter
    def radius(self,value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @redius.deleter
    def name(self):
        print("Deleting name...")
        del self._name
        