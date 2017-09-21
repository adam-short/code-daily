import string
from string import ascii_uppercase as ups, ascii_lowercase as lows

def shift_char_by(char, newups, newlows):
    # access ascii_uppercase array via char position + shift, wrapped for overflows.
    try:
        pos = ups.index(char.upper())
    except: # if an error is raised, return char (cos its not a letter)
        return char

    # return from appropriate array.
    return newups[pos] if char in ups else newlows[pos]

def shift_string_by(strng, newups, newlows):
    shifted = [shift_char_by(x, newups, newlows) for x in list(strng)]
    return ''.join(shifted)

inp = raw_input("string >>    ")
alphabet = list(raw_input("enter deranged alphabet by >>    "))
print(shift_string_by(inp, map(string.upper, alphabet), map(string.lower, alphabet)))
