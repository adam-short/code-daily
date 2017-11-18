import sys

ALPHABET = {
    ".-" : "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}

def morse2letter(morse):
    print(morse)
    try:
        return ALPHABET[morse]
    except KeyError as e:
        return "?"

def morse2word(morse_word):
    print(morse_word.split(' '))
    return ''.join([morse2letter(l) for l in morse_word.split(' ')])

def translate(morse_sentence):
    return ''.join([morse2word(w) for w in morse_sentence])

def break_on_slash(inp):
    return inp.split(' / ')

def decrypt(inp):
    morse_sentence = break_on_slash(inp)
    translated = translate(morse_sentence)
    return translated

def encrypt(inp):
    reverse = {v: k for k, v in ALPHABET.iteritems()}
    words = inp.upper().split(' ')
    res = []
    for w in words:
        res.append(' '.join([reverse[l] for l in list(w)]))

    return ' / '.join(res)





if __name__ == '__main__':
    try:
        if sys.argv[2] == '-d':
            print(decrypt(sys.argv[1]))
        elif sys.argv[2] == '-e':
            print(encrypt(sys.argv[1]))
    except IndexError as e:
        print("You are missing an argument.")
