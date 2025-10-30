[繁體中文󠄁](https://github.com/haydenwong7bm/inherited-glyphs-converter/blob/main/README_zh-tc.md) **简体中文󠄁** [English](https://github.com/haydenwong7bm/inherited-glyphs-converter/blob/main/README.md)

* [网上版已推出，请点击我！](https://haydenwong7bm.github.io/inherited-glyphs-converter/zh-sc/)

# 传承字形转換器
 转換汉字至[传承字形](https://zh.wikipedia.org/wiki/%E8%88%8A%E5%AD%97%E5%BD%A2)（大致根据[《传承字形检校󠄁表》](https://github.com/ichitenfont/inheritedglyphs)标准），消󠄁除[新字形](https://zh.wikipedia.org/wiki/%E6%96%B0%E5%AD%97%E5%BD%A2)、[香港󠄁](https://zh.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E5%AD%97%E5%AD%97%E5%BD%A2%E8%A1%A8)及󠄁[台湾](https://zh.wikipedia.org/wiki/%E5%9C%8B%E5%AD%97%E6%A8%99%E6%BA%96%E5%AD%97%E9%AB%94)地区标准字形，及󠄁于Unicode[可统一但被分󠄁开编码](https://gitee.com/eisoch/irg/issues/I5FR1Q)的󠄁汉字。
 
 此转換器会尽量保留[新字体](https://zh.wikipedia.org/wiki/%E6%96%B0%E5%AD%97%E4%BD%93)及󠄁[简化󠄁字](https://zh.wikipedia.org/wiki/%E7%AE%80%E5%8C%96%E5%AD%97)。
 
 ## 使󠄁用方法
 
 ### 命令行
 
	python . <文󠄁本文󠄁件名称>
 
 命令行选项：
 
 | **选项** | **功能** | **预设値** |
 |---|---|---|
 | `-c` | 一个含有`'j'`、`'k'`及󠄁／或`'t'`的󠄁字符串，或者`_`。<br>`j`：使󠄁用日本[兼󠄁容表意󠄁文󠄁字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)。<br>`k`：使󠄁用韩国兼󠄁容表意󠄁文󠄁字。<br>`t`：使󠄁用[CNS 11643兼󠄁容表意󠄁文󠄁字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E8%A3%9C%E5%85%85%E5%8D%80)。<br>`_`：不使󠄁用兼󠄁容表意󠄁文󠄁字。 | jkt |
 | `-s` | 使󠄁用辅助平󠄁面字符設定，参数値如下：<br>`c`：只使󠄁用已包󠄁括於Adobe-Japan1、HKSCS或[UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf)的󠄁字符。<br>`*`：使󠄁用所󠄁有字符。<br>`_`：只使󠄁用基本平󠄁面字符。 | c |
 | `-n` | 不转換Unicode不能统一的󠄁字。（例如：秘 → 祕、床 → 牀） | |
 | `-v` | 使󠄁用不符合字理唯常见的󠄁异体写法。（例如：免 → 免） | |
 | `-a` | 使󠄁用更󠄁符合字理的󠄁异体写法。（例如：皆 → 𣅜） | |
 | `-i` | 使󠄁用异体字选择器串行转換。参数列表：<br>`ad`：[Adobe-Japan1异体字选择器串行](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf)。<br>~~`mo`：[Moji-Joho异体字选择器串行](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf)。~~<br>`ms`：[澳门增补字符集异体字选择器串行](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_MSARG.pdf)。 | |
 | `-t` | 使󠄁用含有饰笔捺的󠄁异体字选择器串行转換。 | |
 | `-p` | 把标点符号置中。 | |
 | `-u` | 指定字符编码解码。 | `utf-8` |
 
 ### 导入模组
 
 `inheritedglyphs`模组提供了一个函数`convert()`，此函数会转換字符串至传承字形。
 
 函数参数：
 
 | **参数** | **功能** | **预设値** |
 |---|---|---|
 | `compatibility` | 一个含有`'j'`、`'k'`、及󠄁／或`'t'`的󠄁可叠代对象。<br>`'j'`：使󠄁用日本[兼󠄁容表意󠄁文󠄁字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)。<br>`'k'`：使󠄁用韩国兼󠄁容表意󠄁文󠄁字。<br> `'t'`：使󠄁用[CNS 11643兼󠄁容表意󠄁文󠄁字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97%E8%A3%9C%E5%85%85%E5%8D%80)。 | `['j', 'k', 't']` |
 | `supp_planes` | 使󠄁用辅助平󠄁面字符設定，参数値如下：<br>`c`：只使󠄁用已包󠄁括于Adobe-Japan1、HKSCS或[UnihanCore2020](https://www.unicode.org/L2/L2019/19388-unihan-core-2020.pdf)的󠄁字符。<br>`*`：使󠄁用所󠄁有字符。<br>`False`：只使󠄁用基本平󠄁面字符。 | `'c'` |
 | `convert_not_unifiable` | 如设为`True`，将转換Unicode不能统一的󠄁字。（例如：秘 → 祕、床 → 牀） | `True` |
 | `alternate` | 使󠄁用不符合字理唯常見的󠄁异體写法。（例如：免 → 免） | `False` |
 | `etymological` | 使󠄁用更󠄁符合字理的󠄁异体写法。（例如：皆 → 𣅜） | `False` |
 | `ivs` | 使󠄁用异体字选择器串行转換。参数値为含有以下字符串的󠄁可迭󠄁代对象或`False`：<br>`'ad'`：使󠄁用[Adobe-Japan1异体字选择器串行](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Adobe-Japan1.pdf)。<br>~~`'mo'`：使󠄁用[Moji-Joho异体字选择器串行](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_Moji_Joho.pdf)。~~<br>`'ms'`：使󠄁用[澳门增补字符集异体字选择器串行](https://unicode.org/ivd/data/2022-09-13/IVD_Charts_MSARG.pdf)。 | `False` |
 | `tiao_na` | 使󠄁用含有饰笔捺的󠄁异体字选择器串行转換。 | `True` |
 | `punctation_align_center` | 把标点符号置中。 | `False` |
 
 ### 使󠄁用例子
 
	>>> from inheritedglyphs import *
	>>> string = '寒來暑往，秋收冬藏。閏餘成歳，律吕調陽。雲騰致雨，露結為霜。金生麗水，玉出崑崗。'
	>>> print(convert(string))
	寒來暑往，秋收冬藏。閏餘成歲，律呂調陽。雲騰致雨，露結爲霜。金生麗水，玉出崑崗。
	>>> print(convert(string, compatibility='j')) # 不使󠄁用韩󠄁国及󠄁CNS兼容表意󠄁文󠄁字
	寒來暑往，秋收冬藏。閏餘成歲，律呂調陽。雲騰致雨，露結爲霜。金生麗水，玉出崑崗。
	>>> print(convert(string, compatibility=False, ivs=['ad'])) # 只使用Adobe-Japan1异体字选择器
	寒󠄁來暑󠄁往󠄁，秋收冬󠄀藏。閏餘成󠄁歲，律呂調󠄁陽。雲騰󠄁致雨，露結爲霜。金生麗󠄁水，玉出崑崗。

 ### 下载及󠄁安装

 该模组需要Python 3.7或更󠄁高版本。
 
 如使用pip安装最新版本，只需执行：
	pip install inheritedglyphs
 或于源码主目彔：
	pip install .
 