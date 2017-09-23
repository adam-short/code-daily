import sys
import itertools

def consecutives(words):
    return [list(g) for k, g in itertools.groupby(words)]

def string_from_nth_places(char_tuples, n):
    return ''.join(x[n] for x in char_tuples if len(x)>=n+1)

def duplicate_to_seperates(words):
    cons = consecutives(words)
    seperates = []
    for n in range(len(max(cons, key=len))):
        seperates.append(string_from_nth_places(cons, n))
    return seperates


print(duplicate_to_seperates(sys.argv[1]))
