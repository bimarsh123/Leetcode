def plusOne(digits):
  n=len(nums)
  for i in range(n-1,-1,-1):
    if(digits[i]==9):
      digits[i]=0
    else:
      digits[i]+=1
      return digits
  digits.append(0)
  digits[0]=1
  return digits
