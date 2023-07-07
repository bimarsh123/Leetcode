def removeduplicates(nums):
    j=0
    for i in range(1,len(nums)):
        if(nums[j]!=nums[i]):
            nums[j+1]=nums[i]
            j+=1
    return j+1
print(removeduplicates([1,1,2]))
print(removeduplicates([0,0,1,1,1,2,2,3,3,4]))
