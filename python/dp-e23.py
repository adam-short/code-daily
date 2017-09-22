import itertools

def half_split(ls):
    middle = len(ls) / 2
    return ls[0:middle], ls[middle:]


print(half_split([1,2,3,4,5,6,7,8,9]))
