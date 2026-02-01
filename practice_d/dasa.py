from itertools import permutations

given = ['a','b','c','d']

allcombi = list(permutations(given))

allcombi=[''.join(curr) for curr in allcombi]

print(allcombi)




