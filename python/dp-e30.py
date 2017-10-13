import itertools
import sys

# takes a list of ints + target number.
#   --> 2 ints that sum to target number, or None

def pair_sums(ls):
    for pair in itertools.permutations(ls, 2):
        yield (pair[0] + pair[1], pair)

target = int(sys.argv[1])
ls = map(int, sys.argv[2].split(" "))

print next((pair[1] for pair in pair_sums(ls) if pair[0] == target), None)
