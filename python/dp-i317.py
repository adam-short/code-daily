import re
import sys

# Doesn't do brackets like the original question
#TODO: Add bracket support.


element = re.compile(r'([A-Z]{1}[a-z]*\d*)')
element_multiplier = re.compile('\d+')

def findall_elements(string):
    print(string)
    return element.findall(string)

def elgroup2atom(elgroup):
    num_match = element_multiplier.search(elgroup)
    print("{} : {}".format(elgroup, num_match))
    return int(num_match.group(0)) if num_match else 1

def atom_sum(elementstr):
    elements = findall_elements(elementstr)
    print(elements)
    quantity = [elgroup2atom(el) for el in elements]

    return sum(quantity)

if __name__ == '__main__':
    try:
        print(atom_sum(sys.argv[1]))
    except IndexError as e:
        print("ERROR: Missing argument.")
