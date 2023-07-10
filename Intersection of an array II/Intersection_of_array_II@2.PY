
def intersect(nums1,nums2):
    nums1=sorted(nums1)
    nums2=sorted(nums2)
    li=[]
    m,n=len(nums1),len(nums2)
    l=h=0
    while(l< m and h < n):
        if(nums1[l]>nums2[h]):
            h+=1
        elif(nums1[l]<nums2[h]):
            l+=1
        else:
            li.append(nums1[l])
            l+=1
            h+=1
    return li


print(intersect([1,2,2,1],[2,2]))

