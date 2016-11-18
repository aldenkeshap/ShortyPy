import re
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

replacements = {
    'False':'Ⓕ', 'True':'Ⓣ', 'None':'Ⓝ', 'and':'ⓐ', 'as':'ⓢ', 'assert':'Ⓐ',
    'break':'ⓑ', 'class':'ⓒ', 'continue':'Ⓒ', 'def':'ⓓ', 'del':'Ⓓ',
    'elif':'ⓔ',  'else':'Ⓔ', 'except':'ⓧ', 'finally':'ⓕ', 'for':'Ⓞ',
    'from':'ⓡ', 'global':'ⓖ', 'if':'ⓘ', 'import':'ⓜ', 'in':'ⓩ', 'is':'Ⓩ',
    'lambda':'ⓛ', 'nonlocal':'Ⓝ', 'not':'ⓝ', 'or':'ⓞ', 'pass':'ⓟ',
    'raise':'Ⓡ', 'return':'ⓡ', 'try':'ⓣ', 'while':'ⓦ', 'with':'Ⓦ',
    'yeild':'ⓨ', 'abs':'ａ', 'all':'ｂ', 'any':'ｃ', 'ascii':'ｄ', 'bin':'ｅ',
    'bool':'ｆ', 'bytearray':'ｇ', 'bytes':'ｈ', 'callable':'ｉ', 'chr':'ｊ',
    'classmethod':'ｋ', 'compile':'ｌ', 'complex':'ｍ', 'delattr':'ｎ',
    'dict':'ｏ', 'dir':'ｐ', 'divmod':'ｑ', 'enumerate':'ｒ', 'eval':'ｓ',
    'exec':'ｔ', 'filter':'ｕ', 'float':'ｖ', 'format':'ｗ', 'frozenset':'ｘ',
    'getattr':'ｙ', 'globals':'ｚ', 'hasattr':'Ａ', 'hash':'Ｂ', 'help':'Ｃ',
    'hex':'Ｄ', 'id':'Ｅ', 'input':'Ｆ', 'int':'Ｇ', 'isinstance':'Ｈ',
    'issubclass':'Ｉ', 'iter':'Ｊ', 'len':'Ｋ', 'list':'Ｌ', 'locals':'Ｍ',
    'map':'Ｎ', 'max':'Ｏ', 'memoryview':'Ｐ', 'min':'Ｑ', 'next':'Ｒ',
    'object':'Ｓ', 'oct':'Ｔ', 'open':'Ｕ', 'ord':'Ｖ', 'pow':'Ｗ', 'print':'Ｘ',
    'property':'Ｙ', 'range':'Ｚ', 'repr':'１', 'reversed':'２', 'round':'３',
    'set':'４', 'setattr':'５', 'slice':'６', 'sorted':'７', 'staticmethod':'８',
    'str':'９', 'sum':'！', 'super':'＠', 'tuple':'＃', 'type':'＄', 'vars':'％',
    'zip':'＾', '__import__':'＆'
}
changed = True
while changed:
    textCopy = text
    text = text.replace('\n\n', '\n')
    changed = text != textCopy

text = re.sub(r'from (.+) import \*', r'Ⓘ\1', text)
newlist = replacements.items()
sortedlist = sorted(newlist, key=lambda s: len(s[0]))[::-1]
print(sortedlist)
for whole in sortedlist:
    copy = text
    key, value = whole
    text = text.replace(key, value)
    if copy == text: print(key, value)
outputOrFile = input('Output or file: ')
if outputOrFile[0].lower() == 'f':
    if textOrFile[0].lower() == 'f': sameOrDifferent = input('Same file: ')
    if sameOrDifferent[0].lower() == 'y':
        file = open(fileName, 'w')
        file.write(text)
        file.close()
    else:
        file = open(input('File to write to: '), 'w')
        file.write(text)
        file.close()
elif outputOrFile[0].lower() == 'o':
    print('Your code:')
    print(text, end='')
