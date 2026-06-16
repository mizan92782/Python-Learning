from collections import OrderedDict
d1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

d1['t']=6
d1['e']=4
# mote to end
d1.move_to_end('a')

#deleting element

d1.pop('b')

for k, v in d1.items():
    print(k, v)