from itertools import groupby
import sys

# The vowel subsequences in the word codewarriors are o,e,a,io. The longest of
# these has a length of 2. Given a lowercase string that has alpahbetic characters
# only and no spaces, return the length of the longest vowel subsequence.

def longest_vowel_subsequence_in(word):
    l, top = 0, 0
    for w in word[1:]:
        if w in 'aeiou':
            l += 1
        else:
            top = l if l > top else top
            l = 0
    return top

print longest_vowel_subsequence_in(sys.argv[1])
