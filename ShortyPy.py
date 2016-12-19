# -*- coding: utf-8 -*-
import re
from charMapping import *
replacements = charToFunc

textOrFile = input('Text or file: ')
if textOrFile[0].lower() == 'f':
    fileName = input('File to execute: ')
    file = open(fileName)
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

changed = True
while changed:
    textCopy = text
    text = text.replace('\n\n', '\n')
    changed = text != textCopy

text = re.sub(r'Ｋ(.+)', r'from \1 import *', text)
newlist = replacements.items()

sortedlist = sorted(replacements, key=lambda s:len(replacements[s]), reverse=True)[::-1]
for key in sortedlist:
    value = replacements[key]
    text = text.replace(key, value)

exec(text)
