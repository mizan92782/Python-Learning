from collections import namedtuple



Point = namedtuple('Point',['x','y'])

points= [
    Point(x=4,y=3),
    Point(x=9,y=4.4),
    Point(x=2,y=2.2)
]


print(points)



print("Iteration : ----------")

for x in points:
    print(f"Point to {x.x} and {x.y}")