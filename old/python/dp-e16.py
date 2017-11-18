import re

target = raw_input("Enter string >  ")
replaceables = re.compile("["+raw_input("Enter replaceables >  ")+"]")
print(replaceables.sub('', target))
