import re
import sys

correct_format = re.compile('\(*\d{3}\)*[-. ]*\d{3}[-. ]*\d{4}$')

def is_valid(number):
    return True if correct_format.match(number) else False

if __name__ == '__main__':
    try:
        print(is_valid(sys.argv[1]))
    except IndexError as e:
        print("ERROR: Missing an MSN.")
