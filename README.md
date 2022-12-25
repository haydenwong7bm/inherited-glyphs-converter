# inherited-glyphs-converter
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
 | `-s <value>` | If `value` is `c`: Use only [UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf) characters on supplementary planes.
 if `value` is `*`: Use all characters on supplementary planes. | `c` |
 | `-i` | Convert other inherited variants (e.g. 秘 → 祕, 裡 → 裏). | `True` |
 
 ### Import module
 The `inheritedglyphs` module provides a single function `convert()` which converts a string to their inherited glyphs form.
 
 Function arguments:
 
 | **Arguments** | **Usage** | **Default value** |
 |---|---|
 | `use_compatibility` | An iterable that contains `'j'`, `'k'`, and/or `'t'`.
 `'j'`: Use Japanese [compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs).
 `'k'`: Use Korean compatibility ideographs.
 `'t'`: Use [CNS 11643 compatibility ideographs](https://en.wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement). | `'jkt'` |
 | `convert_inherited` | If `True`, it will convert other inherited variants (e.g. 秘 → 祕, 裡 → 裏). | `True` |
 | `use_supp` | Either be `False`, `'c'`, `'*'`. If `c`, it can use only [UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf) characters on supplementary planes. If `'*'`, it can use all characters on supplementary planes. | `'c'` |
 
	>>> from inheritedglyphs import *
	>>> string = '李白（唐‧五言絕句）《靜夜思》：「牀前明月光，疑是地上霜，擧頭望明月，低頭思故鄕。」'
	>>> print(convert(string))
	李白（唐‧五言絕句）《靜夜思》：「牀前明月光，疑是地上霜，擧頭望明月，低頭思故鄕。」
	>>> print(convert(string, use_compatibility='jt')) # don't use Korean compatibility ideographs
	李白（唐‧五言絕句）《靜夜思》：「牀前明月光，疑是地上霜，擧頭望明月，低頭思故鄕。」
	>>> print(convert(string, convert_inherited=False))
	李白（唐‧五言絕句）《靜夜思》：「床前明月光，疑是地上霜，擧頭望明月，低頭思故鄕。」
	
# 傳承字形轉換器
 轉換中文文字至[傳承字形](https://zh.wikipedia.org/wiki/%E8%88%8A%E5%AD%97%E5%BD%A2)（大致根據[《傳承字形檢校表》](https://github.com/ichitenfont/inheritedglyphs)標準），消除[新字形](https://zh.wikipedia.org/wiki/%E6%96%B0%E5%AD%97%E5%BD%A2)、[香港](https://zh.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E5%AD%97%E5%AD%97%E5%BD%A2%E8%A1%A8)及[臺灣](https://zh.wikipedia.org/wiki/%E5%9C%8B%E5%AD%97%E6%A8%99%E6%BA%96%E5%AD%97%E9%AB%94)標準異體字，如該異體字於Unicode[分開編碼](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%B5%B1%E4%B8%80%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97#%E8%AA%8D%E5%90%8C%E5%8E%9F%E5%89%87%E8%88%87%E5%8E%9F%E5%AD%97%E9%9B%86%E5%88%86%E9%9B%A2%E5%8E%9F%E5%89%87)。
 
 此轉換器會儘量保留[新字體](https://zh.wikipedia.org/wiki/%E6%96%B0%E5%AD%97%E4%BD%93)及[簡化字](https://zh.wikipedia.org/wiki/%E7%AE%80%E5%8C%96%E5%AD%97)。
 
 ## 使用
 
 ### 命令列
 
	python . <檔案名稱>
 
 命令列選項：
 
 | **選項** | **功能** |
 |---|---|
 | `-j` | 使用日本[相容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)。 |
 | `-k` | 使用韓國相容表意文字。 |
 | `-t` | 使用[CNS 11643相容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E8%A3%9C%E5%85%85%E5%8D%80)。 |
 | `-r` | 不轉換其他異體字（例如：舉 → 擧、裡 → 裏） |
 | `-sc` | 不使用於輔助平面中的[UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf)字符。 |
 | `-s` | 使用於輔助平面中的字符，此選項亦會禁用`-sc`選項。 |
 
 ### 導入模組
 
 `inheritedglyphs`模組提供了一個函數`convert()`，此函數會轉換字串至傳承字形。
 
 函數選項：
 
 | **選項** | **功能** |
 |---|---|
 | `use_j` | 如設爲`True`，將使用日本[相容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)。 |
 | `use_k` | 如設爲`True`，將使用韓國相容表意文字。 |
 | `use_t` | 如設爲`True`，將使用[CNS 11643相容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E8%A3%9C%E5%85%85%E5%8D%80)。 |
 | `convert_variants` | 如設爲`True`，將不轉換其他異體字（例如：舉 → 擧、裡 → 裏） |
 | `use_supp_core` | 如設爲`True`，將不使用於輔助平面中的[UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf)字符。 |
 | `use_supp_planes` | 如設爲`True`，將使用於輔助平面中的字符。 |
 
	>>> from inheritedglyphs import *
	>>> print(convert('逹至奥林匹克精神的秘訣'))
	達至奧林匹克精神的祕訣
	>>> print(convert('逹至奥林匹克精神的秘訣', use_j=True))
	達至奧林匹克精神的祕訣
	>>> print(convert('逹至奥林匹克精神的秘訣', convert_variant=False))
	達至奧林匹克精神的秘訣