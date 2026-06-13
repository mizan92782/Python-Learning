from functools import reduce
import operator
a = [1, 3, 5, 6, 2]


sum = reduce(operator.add,a)
print(sum)