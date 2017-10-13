import itertools
import math

def itertool_way(ls):
    res = sorted([list(g) for k, g in itertools.groupby(ls)], key=len)
    return res[-1][0]


target = sorted(range(10000000)+[9985])
print "Target created. Goal is 9985."
print "Trying itertool_way"
print itertool_way(target)
