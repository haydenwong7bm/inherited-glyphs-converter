# inherited-glyphs-converter
 Convert text with CJK characters to their [inherited glyphs](https://en.wikipedia.org/wiki/Jiu_zixing) form, eliminating the [xin zixing](https://en.wikipedia.org/wiki/Xin_zixing), [Hong Kong](https://en.wikipedia.org/wiki/List_of_Graphemes_of_Commonly-Used_Chinese_Characters) and [Taiwan](https://en.wikipedia.org/wiki/Standard_Form_of_National_Characters) standard variant if that character variant is [encoded seperately](https://en.wikipedia.org/wiki/CJK_Unified_Ideographs#CJK_Unified_Ideographs) on Unicode.
 
 Note that the converter will keep [Shinjitai](https://en.wikipedia.org/wiki/Shinjitai) and [simplified Chinese characters](https://en.wikipedia.org/wiki/Simplified_Chinese_characters) as much as possible.
 
 ## Usage
 
 ### Command line
 
	python . <file name>
 `-j` flag for using Japanese unifiable variants and `-k` flag for using Korean unifiable variants. `-r` for _not_ converting other inherited variants (e.g. 舉 → 擧)
 
 ### Import module
 The `inheritedglyphs` module provides a single function `convert()` which converts a string to their inherited glyphs form.
 
 To use Japanese compatibility variants, specify `use_j=True`. For Korean compatibility variants, specify `use_k=True`. For _not_ converting other inherited variants, specify `use_inherited=False`.
 
    >>> from inheritedglyphs import *
    >>> print(convert('逹至奥林匹克精神的秘訣'))
    達至奧林匹克精神的祕訣
    >>> print(convert('逹至奥林匹克精神的秘訣', use_j=True))
    達至奧林匹克精神的祕訣
	>>> print(convert('逹至奥林匹克精神的秘訣', use_inherited=False))
    達至奧林匹克精神的秘訣
	