# -*- coding: utf-8 -*-
chars =  ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-=~!@#$%^&*()_[]{}'",.<>?|/\°¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾\nⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ⓪①②③④⑤⑥⑦⑧⑨ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９－＝～！＠＃＄％＾＆＊（）＿［］｛｝＇＂，．＜＞？／＼'''
charToFunc = {'ⓐ':'False', 'ⓑ':'None', 'ⓒ':'True', 'ⓓ':'__import__(', 'ⓔ':'abs(', 'ⓕ':'all(', 'ⓗ':'any(', 'ⓙ':'ascii(', 'ⓛ':'bin(', 'ⓜ':'bool(', 'ⓞ':'bytearray(', 'ⓟ':'bytes(', 'ⓠ':'callable(', 'ⓡ':'chr(', 'ⓣ':'classmethod(', 'ⓤ':'compile(', 'ⓥ':'complex(', 'ⓩ':'delattr(', 'Ⓐ':'dict(', 'Ⓑ':'dir(', 'Ⓒ':'divmod(', 'Ⓕ':'enumerate(', 'Ⓖ':'eval(', 'Ⓘ':'exec(', 'Ⓙ':'filter(', 'Ⓛ':'float(', 'Ⓝ':'format(', 'Ⓟ':'frozenset(', 'Ⓠ':'getattr(', 'Ⓢ':'globals(', 'Ⓣ':'hasattr(', 'Ⓤ':'hash(', 'Ⓥ':'help(', 'Ⓦ':'hex(', 'Ⓧ':'id(', '①':'input(', '②':'int(', '④':'isinstance(', '⑤':'issubclass(', '⑥':'iter(', '⑧':'len(', '⑨':'list(', 'ａ':'locals(', 'ｂ':'map(', 'ｃ':'max(', 'ｄ':'memoryview(', 'ｅ':'min(', 'ｆ':'next(', 'ｈ':'object(', 'ｉ':'oct(', 'ｊ':'open(', 'ｌ':'ord(', 'ｎ':'pow(', 'ｏ':'print(', 'ｐ':'property(', 'ｒ':'range(', 'ｓ':'repr(', 'ｔ':'reversed(', 'ｕ':'round(', 'ｖ':'set(', 'ｗ':'setattr(', 'ｘ':'slice(', 'ｙ':'sorted(', 'ｚ':'staticmethod(', 'Ａ':'str(', 'Ｂ':'sum(', 'Ｃ':'super(', 'Ｅ':'tuple(', 'Ｆ':'type(', 'Ｇ':'vars(', 'Ｋ':'zip('}
funcToChar = {'False':'ⓐ', 'None':'ⓑ', 'True':'ⓒ', '__import__(':'ⓓ', 'abs(':'ⓔ', 'all(':'ⓕ', 'any(':'ⓗ', 'ascii(':'ⓙ', 'bin(':'ⓛ', 'bool(':'ⓜ', 'bytearray(':'ⓞ', 'bytes(':'ⓟ', 'callable(':'ⓠ', 'chr(':'ⓡ', 'classmethod(':'ⓣ', 'compile(':'ⓤ', 'complex(':'ⓥ', 'delattr(':'ⓩ', 'dict(':'Ⓐ', 'dir(':'Ⓑ', 'divmod(':'Ⓒ', 'enumerate(':'Ⓕ', 'eval(':'Ⓖ', 'exec(':'Ⓘ', 'filter(':'Ⓙ', 'float(':'Ⓛ', 'format(':'Ⓝ', 'frozenset(':'Ⓟ', 'getattr(':'Ⓠ', 'globals(':'Ⓢ', 'hasattr(':'Ⓣ', 'hash(':'Ⓤ', 'help(':'Ⓥ', 'hex(':'Ⓦ', 'id(':'Ⓧ', 'input(':'①', 'int(':'②', 'isinstance(':'④', 'issubclass(':'⑤', 'iter(':'⑥', 'len(':'⑧', 'list(':'⑨', 'locals(':'ａ', 'map(':'ｂ', 'max(':'ｃ', 'memoryview(':'ｄ', 'min(':'ｅ', 'next(':'ｆ', 'object(':'ｈ', 'oct(':'ｉ', 'open(':'ｊ', 'ord(':'ｌ', 'pow(':'ｎ', 'print(':'ｏ', 'property(':'ｐ', 'range(':'ｒ', 'repr(':'ｓ', 'reversed(':'ｔ', 'round(':'ｕ', 'set(':'ｖ', 'setattr(':'ｗ', 'slice(':'ｘ', 'sorted(':'ｙ', 'staticmethod(':'ｚ', 'str(':'Ａ', 'sum(':'Ｂ', 'super(':'Ｃ', 'tuple(':'Ｅ', 'type(':'Ｆ', 'vars(':'Ｇ', 'zip(':'Ｋ'}

def charCodeToShortyPy(text):
    result = ''
    for char in text:
        result += chars[ord(char)]
    return result
def shortyPyToCharCode(text):
    result = ''
    for char in text:
        result += chr(chars.index(char))
    return result
