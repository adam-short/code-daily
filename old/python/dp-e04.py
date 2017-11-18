import string
import random
from sys import argv

def randchar():
    return random.choice(string.letters)

def randstr(length):
    return ''.join([randchar() for x in xrange(length)])

if __name__ == '__main__':
    amount = int(argv[1]) if len(argv) > 1 else 5
    length = int(argv[2]) if len(argv) > 2 else 5

    for x in xrange(amount):
        print(randstr(length))

    
