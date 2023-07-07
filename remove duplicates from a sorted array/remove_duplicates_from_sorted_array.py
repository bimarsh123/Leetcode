def removeduplicates(nums):
    i,j=0,1
    for j in range(len(nums)):
        if(nums[i]==nums[j]):
            j+=1
        else:
            nums[i+1]=nums[j]
            i+=1
            j+=1
    return i+1
print(removeduplicates([1,1,2]))
print(removeduplicates([0,0,1,1,1,2,2,3,3,4]))
