[繁體中文](https://github.com/haydenwong7bm/inherited-glyphs-converter/) **EN**

* [Online version has been released, click me!](https://haydenwong7bm.github.io/inherited-glyphs-converter/en/)

# Inherited Glyphs Converter
 Convert CJK text to their [inherited glyphs](https://en.wikipedia.org/wiki/Jiu_zixing) form (mostly follows [_List of Recommended Inherited Glyph Components_](https://github.com/ichitenfont/inheritedglyphs)), eliminating the [xin zixing](https://en.wikipedia.org/wiki/Xin_zixing), [Hong Kong](https://en.wikipedia.org/wiki/List_of_Graphemes_of_Commonly-Used_Chinese_Characters) and [Taiwan](https://en.wikipedia.org/wiki/Standard_Form_of_National_Characters) standard variant if that character variant is [encoded seperately](https://en.wikipedia.org/wiki/CJK_Unified_Ideographs#CJK_Unified_Ideographs) on Unicode.
 
 The converter will keep [Shinjitai](https://en.wikipedia.org/wiki/Shinjitai) and [simplified Chinese characters](https://en.wikipedia.org/wiki/Simplified_Chinese_characters) as much as possible.
 
 ## Usage
 
 ### Command line
 
	python . <file name>
	
 Command line arguments:
 
 | **Options** | **Usage** | **Default value |
 |---|---|---|
 | `-c` | A string that contains `j`, `k` or `t`, or `_`.<br>`j`: Use Japanese [compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs).<br>`k`: Use Korean compatibility ideographs.<br>`t`: Use [CNS 11643 compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement).<br>`_`: Not to use compatibility ideographs. | `jkt` |
 | `-s <value>` | If `value` is `c`: Use only [UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf) characters on supplementary planes<br>If `value` is `*`: Use all characters on supplementary planes.<br>If `value` is `_`: Only use characters from the Basic Multilingual Plane. | `c` |
 | `-n` | Convert inherited variants that are not unifiable on Unicode  (e.g. 秘 → 祕, 峰 → 峯). | |
 | `-i` | A sequence of string, which enables IVS conversion.<br>`'aj1'`: Use the [Adobe-Japan1 IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf).<br>`'mj'`: Use the [Moji-Joho IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf). |  |
 | `-p` | Align the punctation to center. | |
 
 ### Import module
 The `inheritedglyphs` module provides a single function `convert()` which converts a string to their inherited glyphs form.
 
 Function arguments:
 
 | **Arguments** | **Usage** | **Default value** |
 |---|---|---|
 | `use_compatibility` | An iterable that contains `'j'`, `'k'`, and/or `'t'`.<br>`'j'`: Use Japanese [compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs).<br>`'k'`: Use Korean compatibility ideographs.<br>`'t'`: Use [CNS 11643 compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement). | `'jkt'` |
 | `convert_inherited` | If `True`, it will convert other inherited variants (e.g. 祕 → 祕, 裡 → 裏). | `True` |
 | `use_supp` | Either be `False`, `'c'`, `'*'`.<br>`c`: in supplementary planes, only use [UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf) characters.<br>`'*'`: in supplementary planes, use all characters. | `'c'` |
 | `use_ivs` | An iterable that contains `'aj1'`, and/or `'mj'`.<br>`'aj1'`: Use the [Adobe-Japan1 IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf).<br>`'mj'`: Use the [Moji-Joho IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf). | `False` |
 
	>>> from inheritedglyphs import *
	>>> string = '寒來暑往，秋收冬藏。閏餘成歳，律吕調陽。雲騰致雨，露結為霜。金生麗水，玉出崑崗。'
	>>> print(convert(string))
	寒來暑往，秋收冬藏。閏餘成歲，律呂調陽。雲騰致雨，露結爲霜。金生麗水，玉出崑崗。
	>>> print(convert(string, use_compatibility='j')) # don't use Korean and CNS compatibility ideographs
	寒來暑往，秋收冬藏。閏餘成歳，律呂調陽。雲騰致雨，露結爲霜。金生麗水，玉出崑崗。