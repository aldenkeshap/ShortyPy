# -*- coding: utf-8 -*-
import re
from charMapping import *
replacements = funcToChar
textOrFile = input('Text or file: ')
if textOrFile[0].lower() == 'f':
    fileName = input('File to convert: ')
    file = open(fileName)
    text = file.read()
    file.close()
elif textOrFile[0].lower() == 't':
    text = ''
    print('Code: ')
    line = True
    while line:
        line = input('')
        text += line+'\n'
    text = text[:-1]

changed = True
while changed:
    textCopy = text
    text = text.replace('\n\n', '\n')
    changed = text != textCopy

text = re.sub(r'from (.+) import \*', r'Ｋ\1', text)
newlist = replacements.items()
sortedlist = sorted(newlist, key=lambda s: len(s[0]))[::-1]
#print(sortedlist)
for whole in sortedlist:
    copy = text
    key, value = whole
    text = text.replace(key, value)
    if copy == text: print(key, value)
outputOrFile = input('Output or file: ')
if outputOrFile[0].lower() == 'f':
    if textOrFile[0].lower() == 'f': sameOrDifferent = input('Same file: ')
    else: sameOrDifferent = 'n'
    if sameOrDifferent[0].lower() == 'y':
        file = open(fileName, mode='w')
        file.write(shortyPyToCharCode(text))
        file.close()
    else:
        file = open(input('File to write to: '), mode='w')
        file.write(shortyPyToCharCode(text))
        file.close()
elif outputOrFile[0].lower() == 'o':
    print('Your code:')
    print(text, end='')
