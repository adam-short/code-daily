import calendar
import math
import sys

try:
    year = int(sys.argv[1])
    century = int(math.ceil(year/100.0))
    if calendar.isleap(year):
        print("Leap Year of century {}".format(century))
    else:
        print("Normal Year of century {}".format(century))
except IndexError:
    print("ERROR: Must give me a year.")
except ValueError:
    print("ERROR: Given year value must be an integer.")
