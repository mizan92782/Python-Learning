
# ====== bothe works accumulatively
# ======= reduce return only final resutl
#======== accumulae return accumulae result

from functools import reduce
from itertools import accumulate
from operator import add

a = [1, 2, 3, 4, 5]


acc= accumulate(a,add)
red = reduce(add,a)


print(list(acc))
print(red)