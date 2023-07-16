both the approach for this problem is done using the hash table
for the first approach we use counter c where we store keys and value of given string s as character and how many times the character has repeated in the string. We loop through enumerate s and check if counter values in s equal 1. I f condition satisfy we return True else return -1

the second approach is similar to the first approach expect it uses dict={} rather than counter. We loop through s and if the specific character in string is not c then we assign dict[i] as true else false
Then we loop through keys and values enumerate string s and if dict[value] satisfy we return True else return -1
