# comes from http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
from functools import cmp_to_key


def problem1(givenlist):
    forsum = 0
    whilesum = 0
    recursionsum = 0

    for i in givenlist:
        forsum += i

    n = 0
    while n < len(givenlist):
        whilesum += givenlist[n]
        n += 1

    def recurse(ls, i, summed):
        if i == len(ls):
            return summed
        else:
            return recurse(ls, i+1, summed+ls[i])

    recursionsum = recurse(givenlist, 0, 0)


    return (forsum, whilesum, recursionsum)


def problem2(list1, list2):
    merged = []

    # simplistic
    for i in zip(list1, list2):
        merged.append(i[0])
        merged.append(i[1])

    return merged

def problem3():
    seq = [0, 1]

    for _ in xrange(100):
        seq.append(seq[-1] + seq[-2])

    return seq

def problem4(ls):
    lss = map(str, ls)
    solution = ""
    
    def comparer(x,y):
        return int(y + x) - int(x + y)

    rankedraw = sorted(lss, key=cmp_to_key(comparer))
    return ''.join(ranked), ''.join(rankedraw)
