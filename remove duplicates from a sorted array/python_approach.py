def removeduplicates(nums):
    nums[:]=sorted(set(nums))
    return len(nums)
print(removeduplicates([1,1,2]))
print(removeduplicates([0,0,1,1,1,2,2,3,3,4]))
