Approach for solving this problem
We can use two pointer algorithm to solve this problem
First, create two pointers i and j where i is the slow pointer and j is the fast pointer. Have j advanced in every iteration, but i advance only when two pointers are on different elements. That means j is increased by 1 when index of i and j are equal both i and j are increased by 1 when the element are not equal. We also replace i+1 element with j element when two numbers are not equal.
