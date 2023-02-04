* [請點擊這裏査看中文版。](https://github.com/haydenwong7bm/inherited-glyphs-converter/)

## [Online version has been released, click me!](https://haydenwong7bm.github.io/inherited-glyphs-converter/en/)

# Inherited Glyphs Converter
 Convert CJK text to their [inherited glyphs](https://en.wikipedia.org/wiki/Jiu_zixing) form (mostly follows [_List of Recommended Inherited Glyph Components_](https://github.com/ichitenfont/inheritedglyphs)), eliminating the [xin zixing](https://en.wikipedia.org/wiki/Xin_zixing), [Hong Kong](https://en.wikipedia.org/wiki/List_of_Graphemes_of_Commonly-Used_Chinese_Characters) and [Taiwan](https://en.wikipedia.org/wiki/Standard_Form_of_National_Characters) standard variant if that character variant is [encoded seperately](https://en.wikipedia.org/wiki/CJK_Unified_Ideographs#CJK_Unified_Ideographs) on Unicode.
 
 The converter will keep [Shinjitai](https://en.wikipedia.org/wiki/Shinjitai) and [simplified Chinese characters](https://en.wikipedia.org/wiki/Simplified_Chinese_characters) as much as possible.
 
 ## Usage
 
 ### Command line
 
	python . <file name>
	
 Command line arguments:
 
 | **Options** | **Usage** | **Default value if `-o` not provided** |
 |---|---|---|
 | `-o` | Set options below if this argument is provided. | |
 | `-j` | Use Japanese [compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs). | `True` |
 | `-k` | Use Korean compatibility ideographs. | `True` |
 | `-t` | Use [CNS 11643 compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement). | `True` |
 | `-s <value>` | If `value` is `c`: Use only [UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf) characters on supplementary planes<br>If `value` is `*`: Use all characters on supplementary planes. | `c` |
 | `-i` | Convert other inherited variants (e.g. 秘 → 祕, 裡 → 裏). | `True` |
 
 ### Import module
 The `inheritedglyphs` module provides a single function `convert()` which converts a string to their inherited glyphs form.
 
 Function arguments:
 
 | **Arguments** | **Usage** | **Default value** |
 |---|---|---|
 | `use_compatibility` | An iterable that contains `'j'`, `'k'`, and/or `'t'`.<br>`'j'`: Use Japanese [compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs).<br>`'k'`: Use Korean compatibility ideographs.<br>`'t'`: Use [CNS 11643 compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement). | `'jkt'` |
 | `convert_inherited` | If `True`, it will convert other inherited variants (e.g. 祕 → 祕, 裡 → 裏). | `True` |
 | `use_supp` | Either be `False`, `'c'`, `'*'`.<br>`c`: in supplementary planes, only use [UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf) characters.<br>`'*'`: in supplementary planes, use all characters. | `'c'` |
 
	>>> from inheritedglyphs import *
	>>> string = '教育及青年發展局是澳門特區政府社會文化司成立的公共部門。'
	>>> print(convert(string))
	敎育及靑年發展局是澳門特區政府社會文化司成立的公共部門。」
	>>> print(convert(string, use_compatibility='j')) # don't use Korean and CNS compatibility ideographs
	敎育及靑年發展局是澳門特區政府社會文化司成立的公共部門。
	>>> string = '李白（唐‧五言絶句）《靜夜思》：「床前明月光，疑是地上霜，舉頭望明月，低頭思故鄉。」'
	>>> print(convert(string, convert_inherited=False))
	李白（唐‧五言絕句）《靜夜思》：「床前明月光，疑是地上霜，擧頭望明月，低頭思故鄕。」