from itertools import chain


# Fancy Version
def mxdiflg(l1, l2):
    diffs = list(chain.from_iterable(
        [[abs(len(x) - len(y)) for x in l1] for y in l2])
    )

    return max(diffs) if len(l1) != 0 and len(l2) != 0 else -1


# Simple Version
def mxdiflg_simple(l1, l2):
    mxdif = 0
    for x in l1:
        for y in l2:
            dif = abs(len(x) - len(y))
            mxdif = dif if dif > mxdif else mxdif
    return mxdif


s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", 
      "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

print mxdiflg(s1, s2)
print mxdiflg_simple(s1, s2)
