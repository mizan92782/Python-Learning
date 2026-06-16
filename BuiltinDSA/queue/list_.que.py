


num = [4,5,3,5,2,3]

print(f" Queue : {num}")

print("Push in Queue --- 55-")
num.append(55)

print("Pop from Queue : ------ ")
num.pop(0)



print("POP full queue : ")

while num:
    x = num[0]
    num.pop(0)
    print(x)