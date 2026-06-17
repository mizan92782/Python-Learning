import heapq

li = [25, 20,34,23,66,33,15, 30, 40]




#make heap(mix heap)
heapq.heapify(li)



#=========== hapify
print("heap queue : ",li)




#heap push

heapq.heappush(li,44)
print(li)


#heap pop
min=heapq.heappop(li)
print(min)
print(li)



# n largest elemenent
maxi = heapq.nlargest(3,li)
mini = heapq.nsmallest(4,li)


print(maxi)
print(mini)