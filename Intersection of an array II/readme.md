The hashtable method uses Counter where we create a counter for any array. Then loop through another array if the number is already stored from the first array in the counter we add it to our list and decrease the value of the counter
c[N]>0 then add and c[N]-=1

For two pointer approach, we start off by sorting both arrays, we keep two pointers i and j on each display and loop through each element on both arrays simultaneously. If the pointer 1 on the first array is less than pointer 2 on the second array we increase the first pointer by 1 and vice versa. Since the array is already sorted the variable inside array has been placed in ascending order. If the element of both array is equal on the same pointer we add the element onto the new list and increment both the pointer by one.
