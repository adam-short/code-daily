import itertools
import bisect
import sys

def lucky_numbers_up_to__inefficent(limit):
    ilist = range(1, limit+1, 2)

    i = 0
    for i in itertools.count(1):
        x = ilist[i]
        if not ilist[x-1::x]:
            break
        else:
            del ilist[x-1::x]

    return ilist

def less_then(a, x):
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def more_then(a, x):
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_lucky_number(n):
    millions = lucky_numbers_up_to__inefficent(5000000)
    if n in set(millions):
        return "{} is a lucky number".format(n)
    less = less_then(millions, n)
    bigger = more_then(millions, n)

    return "{} < {} < {}".format(less, n, bigger)

print(find_lucky_number(int(sys.argv[1])))
