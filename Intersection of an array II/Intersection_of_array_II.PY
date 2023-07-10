from collections import Counter
def intersect(nums1,nums2):
    c=Counter(nums1)
    l=[]
    for x in nums2:
        if(c[x]>0):
            l.append(x)
            c[x]-=1
    return l

print(intersect([1,2,2,1],[2,2]))

