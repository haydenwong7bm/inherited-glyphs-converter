**繁體中文󠄁** [EN](https://github.com/haydenwong7bm/inherited-glyphs-converter/blob/main/README_en.md)

* [網󠄁上版已推出，請󠄁點擊我！](https://haydenwong7bm.github.io/inherited-glyphs-converter/zh-tc/)

# 傳承字形轉換器
 轉換漢字至[傳承字形](https://zh.wikipedia.org/wiki/%E8%88%8A%E5%AD%97%E5%BD%A2)（大致根據[《傳承字形檢校󠄁表》](https://github.com/ichitenfont/inheritedglyphs)標準），消󠄁除[新字形](https://zh.wikipedia.org/wiki/%E6%96%B0%E5%AD%97%E5%BD%A2)、[香港󠄁](https://zh.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E5%AD%97%E5%AD%97%E5%BD%A2%E8%A1%A8)及󠄁[臺灣](https://zh.wikipedia.org/wiki/%E5%9C%8B%E5%AD%97%E6%A8%99%E6%BA%96%E5%AD%97%E9%AB%94)標準異體字，及󠄁於Unicode[可統一但被分󠄁開編󠄁碼](https://gitee.com/eisoch/irg/issues/I5FR1Q)的󠄁漢字。
 
 此轉換器會儘量保留[新字體](https://zh.wikipedia.org/wiki/%E6%96%B0%E5%AD%97%E4%BD%93)及󠄁[簡化󠄁字](https://zh.wikipedia.org/wiki/%E7%AE%80%E5%8C%96%E5%AD%97)。
 
 ## 使󠄁用
 
 ### 命令列
 
	python . <檔案名稱󠄁>
 
 命令列選󠄁項：
 
 | **選󠄁項** | **功能** | **預設値** |
 |---|---|---|
 | `-c` | 一個含有`'j'`、`'k'`及󠄁／或`'t'`的󠄁字串，或者`_`。<br>`j`：使󠄁用日本[相容表意󠄁文󠄁字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)。<br>`k`：使󠄁用韓󠄁國相容表意󠄁文󠄁字。<br>`t`：使󠄁用[CNS 11643相容表意󠄁文󠄁字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E8%A3%9C%E5%85%85%E5%8D%80)。<br>`_`：不使󠄁用相容表意󠄁文󠄁字。 | `jkt` |
 | `-s <value>` | 如`value`爲`c`：於輔助平󠄁面中，只使󠄁用[UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf)字符。<br>如`value`爲`*`：於輔助平󠄁面中，使󠄁用所󠄁有字符。<br>如`value`爲`_`：只使󠄁用基本平󠄁面字符。 | `c` |
 | `-n` | 轉換Unicode不能統一的󠄁字（例如：秘 → 祕、峰 → 峯） | `True` |
 | `-v` | 選󠄁用常見異體傳承字形（例如：益 → 益、免 → 免）。 | `False` |
 | `-i` | 選󠄁用異體字選󠄁擇器序列轉換。參數列表：<br>`'ad'`：使󠄁用[Adobe-Japan1異體字選󠄁擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf)。<br>~~`'mo'`：使󠄁用[Moji-Joho異體字選󠄁擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf)。~~<br>`'ms'`：使󠄁用[澳門增補字符集異體字選󠄁擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_MSARG.pdf)。 | |
 | `-p` | 把標點符號置中。 | `False` |
 
 ### 導󠄁入模組
 
 `inheritedglyphs`模組提供了一個函數`convert()`，此函數會轉換字串至傳承字形。
 
 函數參數：
 
 | **參數** | **功能** | **預設値** |
 |---|---|---|
 | `compatibility` | 一個含有`'j'`、`'k'`、及󠄁／或`'t'`的󠄁可疊代者物件。<br>`'j'`：使󠄁用日本[相容表意󠄁文󠄁字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)。<br>`'k'`：使󠄁用韓󠄁國相容表意󠄁文󠄁字。<br> `'t'`：使󠄁用[CNS 11643相容表意󠄁文󠄁字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E8%A3%9C%E5%85%85%E5%8D%80)。 | `['j', 'k', 't']` |
 | `convert_not_unifiable` | 如設爲`True`，將轉換其他異體字（例如：秘 → 祕、峰 → 峯） | `True` |
 | `supp_planes` | 參數値可爲`False`、`'c'`、或`'*'`。<br>`c`：於輔助平󠄁面中，只使󠄁用[UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf)字符。<br>`*`：於輔助平󠄁面中，使󠄁用所󠄁有字符。 | `'c'` |
 | `ivs` | 參數値爲含有以下字串的󠄁可迭󠄁代物件或`False`。<br>`'ad'`：使󠄁用[Adobe-Japan1異體字選󠄁擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf)。<br>~~`'mo'`：使󠄁用[Moji-Joho異體字選󠄁擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf)。~~<br>`'ms'`：使󠄁用[澳門增補字符集異體字選󠄁擇器序列](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_MSARG.pdf)。 | `False` |
	
	>>> from inheritedglyphs import *
	>>> string = '寒來暑往，秋收冬藏。閏餘成歳，律吕調陽。雲騰致雨，露結為霜。金生麗水，玉出崑崗。
	>>> print(convert(string))
	寒來暑往，秋收冬藏。閏餘成歲，律呂調陽。雲騰致雨，露結爲霜。金生麗水，玉出崑崗。
	>>> print(convert(string, compatibility='j')) # 不使󠄁用韓󠄁國及󠄁CNS相容表意󠄁文󠄁字
	寒來暑往，秋收冬藏。閏餘成歳，律呂調陽。雲騰致雨，露結爲霜。金生麗水，玉出崑崗。
	>>> print(convert(string, compatibility=False, use_ivs=['ad'])) # 只使用Adobe-Japan1異體字選󠄁擇器
	寒󠄁來暑󠄁往󠄁，秋收冬󠄀藏。閏餘成󠄁歲，律呂調󠄁陽。雲騰󠄁致雨，露結爲霜。金生麗󠄁水，玉出崑崗
