from itertools import permutations

from numpy.random import permutation
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

result = list(permutations(words))

joined_result = [''.join(p) for p in result]
print(joined_result)

for x in joined_result:
    if x in s:
        print(s.find(x),end=" ")


