def triple_with_given_sum(arr,target):
    
    ans =[]
    hash={}
    
    
    
    for j in range(len(arr)):
        
        for k  in range(j+1,len(arr)):
            
            rem = target-(arr[j]+arr[k])
            
            if rem in hash:
                for i in hash[rem]:
                    ans.append([i,j,k])
    
        if arr[j] not in hash:
            hash[arr[j]]=[]
        hash[arr[j]].append(j)
        
        
    return ans  
        
        
        
        
        
        
        
arr = [0, -1, 2, -3, 1]
target = -2
ans = triple_with_given_sum(arr, target)
for triplet in ans:
    print(triplet[0], triplet[1], triplet[2])