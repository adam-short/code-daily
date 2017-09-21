import itertools

strng = raw_input("Enter small string >  ")
perms = list(itertools.permutations(strng))
perm_strings = [''.join(x) for x in perms]
for permstr in perm_strings:
    print(permstr)
