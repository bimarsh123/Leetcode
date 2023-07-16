#Approach 1
from collections import Counter
def uniqueCharacter(s):
  c=Counter(s)
  for i,j in enumerate(s):
    if(c[j]==1):
      return i
  return -1


#Approach 2
def uniqueCharacter(s):
  dict={}
  for i in s:
    if(i not in dict):
      dict[i]=True
    else:
      dict[i]=False
  for keys, values in enumerate(s):
    if(dict[values]):
      return keys
  return False
