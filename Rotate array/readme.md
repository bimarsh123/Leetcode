The first approach we need to create a new array where we copy the given array as it is. Then we shift the position of element of the array by nums[(i+k)%len(nums)]=new[i]. The exchange is implemented inside a for loop


math Logic approach
In this approach we reverse the array three times
first time we reverse the whole array
second time we reverse from 0th index to k-1 index
third time we reverse from kth index to len of array minus one.
