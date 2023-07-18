def validPalindrome(s):
  i,j=0,len(s)-1
  while(i<j):
    if s[i]==s[j]:
      i+=1
      j-=1
    else:
      return self.isValid(s,i+1,j) or self.isValid(s,i,j-1)
  return True


def isvalid(self,s,i,j):
  while(i<j):
    if s[i]==s[j]:
      i+=1
      j-=1
    else:
      return False
  return True
