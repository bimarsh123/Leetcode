#Method one
def isPalindrome(s):
  i,j=0,len(s)-1
  while(i<j):
    while(i<j and not self.isalpha(s[i]):
      i+=1
    while(j>i and not self.isaplha(s[j]):
      j-=1
    if(s[i].lower()!=s[j].lower()):
      return False
    i,j=i+1,j-1
  return True



def isalpha(self, c):
  return (ord('A') <= ord(c) <=ord('Z') or
          ord('0') <= ord(c) <=ord('9') or
          ord('a') <= ord(c) <=ord('z') )

#Method 2
def isPalindrome(s):
  i,j=0,len(s)-1
  while(i<j):
    if and not self.isalnum(s[j]):
      i+=1
    elif and not self.isalnum(s[j]):
      j-=1
    else:
      if(s[i].lower()!=s[j].lower()):
        return False
      else:
        i,j=i+1,j-1
  return True




