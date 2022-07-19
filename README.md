# inherited-glyphs-converter
 Convert text with CJK characters to their [inherited glyphs](https://en.wikipedia.org/wiki/Jiu_zixing) form, eliminating the [xin zixing](https://en.wikipedia.org/wiki/Xin_zixing), [Hong Kong](https://en.wikipedia.org/wiki/List_of_Graphemes_of_Commonly-Used_Chinese_Characters) and [Taiwan](https://en.wikipedia.org/wiki/Standard_Form_of_National_Characters) standard variant if that character variant is [encoded seperately](https://en.wikipedia.org/wiki/CJK_Unified_Ideographs#CJK_Unified_Ideographs) on Unicode.
 
 Note that the converter will keep [Shinjitai](https://en.wikipedia.org/wiki/Shinjitai) and [simplified Chinese characters](https://en.wikipedia.org/wiki/Simplified_Chinese_characters) as much as possible.
 
 ## Usage
 
 ### Command line
 
	python . <file name>
 `-j` flag for using Japanese unifiable variants and `-k` flag for using Korean unifiable variants. `-r` for _not_ converting other inherited variants (e.g. 舉 → 擧)
 
 ### Import module
 To use Japanese compatibility variants, specify `use_j=True`. For Korean compatibility variants, specify `use_k=True`. For _not_ converting other inherited variants, specify `use_inherited=False`.
 
    >>> from inheritedglyphs import *
    >>> print(convert('奥林匹克精神'))
    奧林匹克精神
    >>> print(convert('奥林匹克精神', use_j=True))
    奧林匹克精神
	