from sets import Set
import sys

s1 = Set(sys.argv[1].split(' '))
s2 = Set(sys.argv[2].split(' '))
print(list(s1 | s2))
