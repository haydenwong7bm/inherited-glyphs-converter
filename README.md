**繁體中文** [EN](https://github.com/haydenwong7bm/inherited-glyphs-converter/blob/main/README_en.md)

* [網上版已推出，請點擊我！](https://haydenwong7bm.github.io/inherited-glyphs-converter/zh-tc/)

# 傳承字形轉換器
 轉換中文文字至[傳承字形](https://zh.wikipedia.org/wiki/%E8%88%8A%E5%AD%97%E5%BD%A2)（大致根據[《傳承字形檢校表》](https://github.com/ichitenfont/inheritedglyphs)標準），消除[新字形](https://zh.wikipedia.org/wiki/%E6%96%B0%E5%AD%97%E5%BD%A2)、[香港](https://zh.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E5%AD%97%E5%AD%97%E5%BD%A2%E8%A1%A8)及[臺灣](https://zh.wikipedia.org/wiki/%E5%9C%8B%E5%AD%97%E6%A8%99%E6%BA%96%E5%AD%97%E9%AB%94)標準異體字，如該異體字於Unicode[分開編碼](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%B5%B1%E4%B8%80%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97#%E8%AA%8D%E5%90%8C%E5%8E%9F%E5%89%87%E8%88%87%E5%8E%9F%E5%AD%97%E9%9B%86%E5%88%86%E9%9B%A2%E5%8E%9F%E5%89%87)。
 
 此轉換器會儘量保留[新字體](https://zh.wikipedia.org/wiki/%E6%96%B0%E5%AD%97%E4%BD%93)及[簡化字](https://zh.wikipedia.org/wiki/%E7%AE%80%E5%8C%96%E5%AD%97)。
 
 ## 使用
 
 ### 命令列
 
	python . <檔案名稱>
 
 命令列選項：
 
 | **選項** | **功能** | **預設値，如不設定`-o`選項** |
 |---|---|---|
 | `-c` | 一個含有`'j'`、`'k'`及／或`'t'`的字串，或者`_`。<br>`j`：使用日本[相容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)。<br>`k`：使用韓國相容表意文字。<br>`t`：使用[CNS 11643相容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E8%A3%9C%E5%85%85%E5%8D%80)。<br>`_`：不使用相容表意文字。 | `jkt` |
 | `-s <value>` | 如`value`爲`c`：於輔助平面中，只使用[UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf)字符。<br>如`value`爲`*`：於輔助平面中，使用所有字符。<br>如`value`爲`_`：只使用基本平面字符。 | `c` |
 | `-i` | 轉換其他異體字（例如：秘 → 祕、裡 → 裏） | `True` |
 | `-I`或`--ivs` | 一組字串，以異體字選擇器序列轉換。<br>`'aj1'`：使用[Adobe-Japan1異體字選擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf)<br>`'mj'`：使用[Moji-Joho異體字選擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf) | `False` |
 
 ### 導入模組
 
 `inheritedglyphs`模組提供了一個函數`convert()`，此函數會轉換字串至傳承字形。
 
 函數參數：
 
 | **參數** | **功能** | **預設値** |
 |---|---|---|
 | `use_compatibility` | 一個含有`'j'`、`'k'`、及／或`'t'`的可疊代者物件。<br>`'j'`：使用日本[相容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)。<br>`'k'`：使用韓國相容表意文字。<br> `'t'`：使用[CNS 11643相容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E8%A3%9C%E5%85%85%E5%8D%80)。 | `['j', 'k', 't']` |
 | `convert_inherited` | 如設爲`True`，將轉換其他異體字（例如：祕 → 祕、裡 → 裏） | `True` |
 | `use_supp` | 參數値可爲`False`、`'c'`、或`'*'`。<br>`c`：於輔助平面中，只使用[UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf)字符。<br>`*`：於輔助平面中，使用所有字符。 | `'c'` |
 | `use_ivs` | 一個含有`'aj1'`及／或`'mj'`的字串。<br>`'aj1'`：使用[Adobe-Japan1異體字選擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf)<br>`'mj'`：使用[Moji-Joho異體字選擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf) | `False` |
 
	>>> from inheritedglyphs import *
	>>> string = '教育及青年發展局是澳門特區政府社會文化司成立的公共部門。'
	>>> print(convert(string))
	夏朝、商朝、西周、東周、秦朝、西漢、東漢、曹魏、西晋、東晋、劉宋、南齊、梁朝、陳朝、隋朝、唐朝、後梁、後唐、後晉、後漢、後周、北宋、南宋、元朝、明朝、淸朝
	>>> print(convert(string, use_compatibility='j')) # 不使用韓國及CNS相容表意文字
	夏朝、商朝、西周、東周、秦朝、西漢、東漢、曹魏、西晋、東晋、劉宋、南齊、梁朝、陳朝、隋朝、唐朝、後梁、後唐、後晋、後漢、後周、北宋、南宋、元朝、明朝、淸朝