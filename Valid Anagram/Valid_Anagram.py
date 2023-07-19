from collections import Counter
def valid_anagram(s,t):
  return (Couter(s)==Counter(t))


def valid_anagram(s,t):
  if(len(s)!=len(t)):
    return False
  CountS,CountT={},{}
  for i in range(len(s)):
    CountS[s[i]]=Counts.get(s[i],0)
    CountT[t[i]]=CountT.get(t[i],0)
  for i in CountS:
    if(CountS[i]!=CountT.get(i,0):
      return False
  return True
