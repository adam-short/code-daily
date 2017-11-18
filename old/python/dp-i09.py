import sys
import itertools

try:
    replaceable, filename, replacer = sys.argv[1:4]
except ValueError:
    print("ERROR: Needs 3 arguments.")
    sys.exit()

with open(filename, 'r+') as f:
    all_words = ''.join(f.readlines()).replace(replaceable, replacer)
    open(filename, 'w').close()
    f.write(all_words)
