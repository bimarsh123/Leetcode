#Hash table
from collections import Counter
def single_number(nums):
    c=Counter(nums)
    for x in nums:
        if(c[x]==1):
            return x


#bit wise operator XOR
def single_number(nums):
    res=0
    for n in nums:
        res^=n
    return res


