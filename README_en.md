[繁體中文](https://github.com/haydenwong7bm/inherited-glyphs-converter/) [简体中文󠄁](https://github.com/haydenwong7bm/inherited-glyphs-converter/blob/main/README_sc.md) **EN**

* [Online version has been released, click me!](https://haydenwong7bm.github.io/inherited-glyphs-converter/en/)

# Inherited Glyphs Converter
 Convert CJK text to their [inherited glyphs](https://en.wikipedia.org/wiki/Jiu_zixing) form (mostly follows [_List of Recommended Inherited Glyph Components_](https://github.com/ichitenfont/inheritedglyphs)), eliminating the [xin zixing](https://en.wikipedia.org/wiki/Xin_zixing), [Hong Kong](https://en.wikipedia.org/wiki/List_of_Graphemes_of_Commonly-Used_Chinese_Characters) and [Taiwan](https://en.wikipedia.org/wiki/Standard_Form_of_National_Characters) standard variant, and character variants that [is unifiable but encoded seperately](https://gitee.com/eisoch/irg/issues/I5FR1Q) on Unicode.
 
 The converter will keep [Shinjitai](https://en.wikipedia.org/wiki/Shinjitai) and [simplified Chinese characters](https://en.wikipedia.org/wiki/Simplified_Chinese_characters) as much as possible.
 
 ## Usage
 
 ### Command line
 
	python . <file name>
	
 Command line arguments:
 
 | **Options** | **Usage** | **Default value** |
 |---|---|---|
 | `-c` | A string that contains `j`, `k` or `t`, or `_`.<br>`j`: Use Japanese [compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs).<br>`k`: Use Korean compatibility ideographs.<br>`t`: Use [CNS 11643 compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement).<br>`_`: Not to use compatibility ideographs. | `jkt` |
 | `-s` | Use of supplementary planes characters settings, parameter follows:<br>`c`: For supplementary planes, only use characters that are in Adobe-Japan1, HKSCS or [UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf) characters on supplementary planes<br>`*`: Use all characters on supplementary planes.<br>`_`: Only use characters from the Basic Multilingual Plane. | `c` |
 | `-n` | Not to convert to inherited variants that are not unifiable on Unicode. (e.g. 秘 → 祕, 床 → 牀). | |
 | `-v` | Use inherited variants that are commonly seen but not etymological. (e.g. 免 → 免). | |
 | `-a` | Use inherited variants that are more etymological. (e.g. 皆 → 𣅜) | |
 | `-i` | Uses IVS when conversion. Parameters:<br>`ad`: Use the [Adobe-Japan1 IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf).<br>~~`mo`: [Moji-Joho IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf).~~<br>`ms`: [Macao Supplementary Character Set IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf). | |
 | `-t` | Uses IVS with tiāo (㇀) nà (㇏) stroke (乀) when conversion. | |
 | `-p` | Center align the punctation. | |
 | `-u` | Specifies text encoding for decoding. | utf-8 |
 
 ### Import module
 
 The `inheritedglyphs` module provides a single function `convert()` which converts a string to their inherited glyphs form.
 
 Function arguments:
 
 | **Arguments** | **Usage** | **Default value** |
 |---|---|---|
 | `compatibility` | An iterable that contains `'j'`, `'k'`, and/or `'t'`.<br>`'j'`: Use Japanese [compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs).<br>`'k'`: Use Korean compatibility ideographs.<br>`'t'`: Use [CNS 11643 compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement). | `'jkt'` |
 | `supp_planes` | Use of supplementary planes characters settings, value follows:<br>`'c'`: for supplementary planes, only use characters in Adobe-Japan1, HKSCS or [UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf).<br>`'*'`: in supplementary planes, use all characters.<br>`False`: Only use characters from the Basic Multilingual Plane. | `'c'` |
 | `convert_not_unifiable` | Convert to inherited variants that are not unifiable on Unicode (e.g. 秘 → 祕, 床 → 牀) | `True` |
 | `alternate` | Use inherited variants that are commonly seen but not etymological. (e.g. 免 → 免) | `False` |
 | `etymological` | Use inherited variants that are more etymological. (e.g. 皆 → 𣅜) | `False` |
 | `ivs` | Uses IVS when conversion. The argument value is an (ordered) iterable that contains one or more of the following, or `False`:<br>`'ad'`: [Adobe-Japan1 IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf).<br>~~`'mo'`: [Moji-Joho IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf).~~<br>`'ms'`: [Macao Supplementary Character Set IVS](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf). | `False` |
 | `tiao_na` | Uses IVS with tiāo (㇀) nà (㇏) stroke (乀) when conversion. | |
 | `-p` | Center align the punctation. | `False` |
 
 # Example
 
	>>> from inheritedglyphs import *
	>>> string = '寒來暑往，秋收冬藏。閏餘成歳，律吕調陽。雲騰致雨，露結為霜。金生麗水，玉出崑崗。'
	>>> print(convert(string))
	寒來暑往，秋收冬藏。閏餘成歲，律呂調陽。雲騰致雨，露結爲霜。金生麗水，玉出崑崗。
	>>> print(convert(string, compatibility='j')) # # don't use Korean and CNS compatibility ideographs
	寒來暑往，秋收冬藏。閏餘成歲，律呂調陽。雲騰致雨，露結爲霜。金生麗水，玉出崑崗。
	>>> print(convert(string, compatibility=False, ivs=['ad'])) # Only uses Adobe-Japan1 IVS
	寒󠄁來暑󠄁往󠄁，秋收冬󠄀藏。閏餘成󠄁歲，律呂調󠄁陽。雲騰󠄁致雨，露結爲霜。金生麗󠄁水，玉出崑崗。
