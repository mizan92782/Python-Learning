from collections import deque

num = [5, 2, 4, 22, 12, 6]

dq = deque(num)  #make deque


# rotate
dq.rotate(1)
print(dq)

while dq:
    x = dq.popleft()
    print(x)




