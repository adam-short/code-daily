from string import ascii_uppercase as ups, ascii_lowercase as lows

def shift_char_by(char, shift):
    # access ascii_uppercase array via char position + shift, wrapped for overflows.
    try:
        pos = (ups.index(char.upper()) + shift) % len(ups)
    except: # if an error is raised, return char (cos its not a letter)
        return char

    # return from appropriate array.
    return ups[pos] if char in ups else lows[pos]

def shift_string_by(strng, shift):
    shifted = [shift_char_by(x, shift) for x in list(strng)]
    return ''.join(shifted)

inp = raw_input("string >>    ")
shift = int(raw_input("shift by >>    "))
print(shift_string_by(inp, shift))
