from itertools import permutations
from operator import itemgetter
import sys

ls = map(int, sys.argv[1].split(" "))
print ls
target = int(sys.argv[2])
perms = list(permutations(ls, 2))
sums = [(g, sum(g)) for g in perms]

print next(s[0] for s in sums if s[1] == target)
