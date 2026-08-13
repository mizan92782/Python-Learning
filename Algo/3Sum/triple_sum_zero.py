#https://www.geeksforgeeks.org/dsa/find-triplets-array-whose-sum-equal-zero/



def findTripletes(arr):
 
 # ans and map
 ans=[]
 hash ={}
 #j value
 for j in range(len(arr)):
     # k  value 
    for k in range(j+1,len(arr)):
        val = -1* (arr[j]+arr[k])

        # find all val before j index that are actulal i index
        if val in hash:
            for i in hash[val]:
                ans.append([i,j,k])
  
  
  
  
  
  
  
  
      #all index add in hash by its  arr[j] value as i index value
    
    if arr[j] not in hash:
        hash[arr[j]]=[]
    hash[arr[j]].append(j)
   
 return ans



if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    res = findTripletes(arr)
    for triplet in res:
        print(triplet[0], triplet[1], triplet[2])
        