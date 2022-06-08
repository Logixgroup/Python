#Letter Matrix 

from itertools import permutations
import enchant

#English words with US locale
dictionary_check=enchant.Dict("en-US")

#emptyList to capture
output=[]

side_char="RTAPRP"
central_char="E"
char_set=side_char+central_char

char_split = [x for x in char_set]

for x in range(4,len(char_set)+1):
    list1 = list(permutations(char_split, x))
    for each_ele in list1:
        if central_char in each_ele:
            capture="".join(each_ele)
            if dictionary_check.check(capture):
      
 #output with duplicates       
  output.append(capture)

print(set(output)) #OnlyUnique prints
