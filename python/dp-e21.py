from itertools import permutations
import sys
import time

def next_biggest(cmp):
    intperms = (int(''.join(x)) for x in permutations(str(cmp)))
    return next(x for x in intperms if x > cmp)

print(next_biggest(int(sys.argv[1])))
