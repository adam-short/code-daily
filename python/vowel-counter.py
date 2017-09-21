import re
from sys import argv as args

def vowel_counter(sentence):
    return len(re.findall(r'[aeiou]', sentence.lower()))

if __name__ == '__main__':
    try:
        print(vowel_counter(args[1]))
    except IndexError:
        print("You need to give me a word/sentence.")
