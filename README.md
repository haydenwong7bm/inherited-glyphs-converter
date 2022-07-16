# inherited-glyphs-converter
 Convert text with CJK characters to their [inherited glyphs](https://en.wikipedia.org/wiki/Jiu_zixing) form from the [xin zixing](https://en.wikipedia.org/wiki/Xin_zixing), [Hong Kong](https://en.wikipedia.org/wiki/List_of_Graphemes_of_Commonly-Used_Chinese_Characters) and [Taiwan](https://en.wikipedia.org/wiki/Standard_Form_of_National_Characters) standard if that variant is [encoded seperately](https://en.wikipedia.org/wiki/CJK_Unified_Ideographs#CJK_Unified_Ideographs) on Unicode.
 It will keep [Shinjitai](https://en.wikipedia.org/wiki/Shinjitai) and [simplified Chinese characters](https://en.wikipedia.org/wiki/Simplified_Chinese_characters) as much as possible.
 
 ## Usage
 
 ### Command line
 
	python . <file name>
 `-j` flag for using Japanese unifiable variants and `-k` flag for using Korean unifiable variants.
 
 ### Import module
    >>> from inheritedglyphs import *
    >>> print(convert('奥林匹克精神'))
    奧林匹克精神
    >>> print(convert('奥林匹克精神', use_j=True)) # use Japanese unifiable variants, for Korean unifiable variants use use_k=True.
    奧林匹克精神
	