a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 3 == 0, a)
print(list(b))




def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b)) # Convert filter object to a list