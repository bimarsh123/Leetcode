def containsNearbyDuplicate(nums,k)->bool:
    dict={}
    for key,value in enumerate(nums):
        if(value in dict and key-dict[value]<=k):
            return True
        dict[value]=key
    return False
    
print(containsNearbyDuplicate([1,0,1,1],1))

