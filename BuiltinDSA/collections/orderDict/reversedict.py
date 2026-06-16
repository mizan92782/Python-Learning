from collections import OrderedDict
d1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])


d1.popitem(last=False)

for k, v in d1.items():
    print(k, v)