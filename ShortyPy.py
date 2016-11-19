import re, codecs
textOrFile = input('Text or file: ')
if textOrFile[0].lower() == 'f':
    fileName = input('File to convert: ')
    file = codecs.open(fileName, encoding='utf-8)
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
text = ''
replacements = {
'Ｎ':'map', '＃':'tuple', 'Ｈ':'isinstance', 'ⓞ':'or', 'ⓩ':'in', 'ⓧ':'except',
'ｎ':'delattr', 'ａ':'abs', 'Ｂ':'hash', 'ｆ':'bool', '＠':'super', '３':'round',
'Ｘ':'print', '５':'setattr', '９':'str', '％':'vars', '！':'sum',
'ｒ':'enumerate', 'Ⓒ':'continue', 'Ｚ':'range', 'ｇ':'bytearray',
'ｚ':'globals', 'Ｖ':'ord', 'ⓛ':'lambda', 'ⓔ':'elif', 'ｋ':'classmethod',
'ｂ':'all', 'ⓕ':'finally', 'Ｇ':'int', 'Ａ':'hasattr', 'ｗ':'format',
'ｔ':'exec', '６':'slice', 'Ｋ':'len', 'ｅ':'bin', 'Ｄ':'hex', 'ⓑ':'break',
'ⓦ':'while', 'ｍ':'complex', 'ⓡ':'from', 'Ⓐ':'assert', '＆':'__import__',
'Ⓣ':'True', 'Ｆ':'input', '７':'sorted', 'Ｔ':'oct', 'Ｒ':'next', 'Ｏ':'max',
'Ⓓ':'del', 'Ⓝ':'None', '１':'repr', 'ｑ':'divmod', 'Ｗ':'pow', 'Ｑ':'min',
'Ⓔ':'else', 'ⓓ':'def', 'ｊ':'chr', 'ⓖ':'global', 'Ⓡ':'raise', 'ｙ':'getattr',
'２':'reversed', 'ｓ':'eval', 'Ｌ':'list', 'ⓜ':'import', 'ｖ':'float',
'ｏ':'dict', 'Ｙ':'property', 'ｈ':'bytes', 'ⓨ':'yeild', 'ｄ':'ascii',
'ｘ':'frozenset', 'Ｓ':'object', '＄':'type', '４':'set', 'ⓣ':'try', 'Ｅ':'id',
'ｌ':'compile', '８':'staticmethod', 'ⓒ':'class', 'Ｉ':'issubclass',
'Ｊ':'iter', 'Ⓕ':'False', 'Ⓦ':'with', 'ⓟ':'pass', '＾':'zip', 'ｉ':'callable',
'Ｍ':'locals', 'ｐ':'dir', 'ｃ':'any', 'ⓝ':'not', 'ⓢ':'as', 'ｕ':'filter',
'Ｃ':'help', 'ⓘ':'if', 'Ｐ':'memoryview', 'ⓐ':'and', 'Ⓩ':'is', 'Ｕ':'open',
'Ⓞ':'for'
}
changed = True
while changed:
    textCopy = text
    text = text.replace('\n\n', '\n')
    changed = text != textCopy

text = re.sub(r'Ⓘ(.+)', r'from \1 import *', text)
newlist = replacements.items()
#sortedlist = list(sorted(lambda s: len(s[0]), key=newlist))[::-1]
sortedlist = sorted(replacements, key=lambda s:len(replacements[s]), reverse=True)[::-1]
for key in sortedlist:
    value = replacements[key]
    text = text.replace(key, value)

exec(text)
