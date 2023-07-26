#Hash table approach using counter
def duplicate(nums):
  c=Counter(nums)
  for i, j in enumerate(nums):
    if(c[j]>1):
      return j
  return -1

#Hash table using dictionary
def duplicate(nums):
  dict={}
  for i, j in enumerate(nums):
    if(j in dict):
      return j
    dict[j]=i
  return -1

#Floyd's algorithm
def duplicate(nums):
  slow=fast=nums[0]
  while True:
    slow=nums[slow]
    fast=nums[nums[fast]]
    if(slow==fast):
      break
  slow=nums[0]
  while slow!=fast:
    slow=nums[slow]
    fast=nums[fast]
  return slow
