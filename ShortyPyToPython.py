# -*- coding: utf-8 -*-
import re
from charMapping import *
textOrFile = input('Text or file: ')
if textOrFile[0].lower() == 'f':
    fileName = input('File to convert: ')
    file = open(fileName, encoding='utf-8')
    text = charCodeToShortyPy(file.read())
    file.close()
elif textOrFile[0].lower() == 't':
    text = ''
    print('Code: ')
    line = True
    while line:
        line = input('')
        text += line+'\n'
    text = text[:-1]

replacements = charToFunc
changed = True
while changed:
    textCopy = text
    text = text.replace('\n\n', '\n')
    changed = text != textCopy
print(text)
input()
text = re.sub(r'Ｋ(.+)', r'from \1 import *', text)
newlist = replacements.items()
sortedlist = sorted(replacements, key=lambda s:len(replacements[s]), reverse=True)[::-1]
for key in sortedlist:
    value = replacements[key]
    text = text.replace(key, value)
outputOrFile = input('Output or file: ')
if outputOrFile[0].lower() == 'f':
    if textOrFile[0].lower() == 'f': sameOrDifferent = input('Same file: ')
    if sameOrDifferent[0].lower() == 'y':
        file = open(fileName, mode='w')
        file.write(text)
        file.close()
    else:
        file = open(input('File to write to: '), mode='w')
        file.write(text)
        file.close()
elif outputOrFile[0].lower() == 'o':
    print('Your code:')
    print(text, end='')
