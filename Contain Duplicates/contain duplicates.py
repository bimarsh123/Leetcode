def containDuplicate(nums)->bool:
    nums=sorted(nums)
    for i in range(1,len(nums)):
        if(nums[i]==nums[i-1]):
            return True
    return False

print(containDuplicate([1,2,3,1]))


