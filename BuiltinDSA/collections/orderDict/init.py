from collections import OrderedDict

od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3

print(list(od.items()))
print(od.keys())
print(od.values())


print(od['apple'])