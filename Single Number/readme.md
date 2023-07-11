Hash table approach is least preferred for this question since we have to use constant space. Having said that though the approach is simple. We simply create a counter table where we stored all the list. We iterate through each element as check if the specific element exist only once. If yes we return the element.

XOR bit wise approach
we determine a variable r=0 we xor r with every element of the list and eventually return the r after the loop ends. The single number return backk as it since the xor of a same number is 0 and xor of single number with zero is the single number
example 
4= 0100
0=0000
0100^0000=01000

2=0010
2=0010

2^2=0000
 
