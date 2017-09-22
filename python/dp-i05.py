import sys
from itertools import chain

def sorted_words_in_file(filestr):
    words = list(chain(*[l.split() for l in filestr]))
    words = map(sorted, words)
    return [''.join(w) for w in words]

def number_of_anagrams(sorted_words):
    uniques = set(sorted_words)
    return sum(1 for x in uniques if sorted_words.count(x) > 1)

with open(sys.argv[1]) as f:
    sorted_words = sorted_words_in_file(f)
    print(number_of_anagrams(sorted_words))
