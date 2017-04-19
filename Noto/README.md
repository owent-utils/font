思源黑体是Google和Adobe联合发布的字体
======

License: Apache License, Version 2.0. 

1. Adobe 开源地址:     https://github.com/adobe-fonts/source-han-sans/
2. Google 官方地址:    http://www.google.com/get/noto/    
3. Google 开源地址:    https://github.com/googlei18n?query=noto

+ Google 字体发布地址：  [Noto Sans CJK(中日韩统一表意文字)](https://github.com/googlei18n/noto-cjk)       [SIL Open Font License, Version 1.1](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)
+ Google 字体发布地址：  [Noto fonts](https://github.com/googlei18n/noto-fonts)        [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

主要使用
======
Windows/Linux使用hinted字体包，macOS使用unhinted字体包。

英文
------
+ Noto Sans （无衬线字体）
+ Noto Serif （有衬线字体）

等宽
------
+ Noto Mono
+ Noto Sans Mono CJK SC

Emoji
------
+ Noto Color Emoji
+ Noto Emoji

中文-思源黑体
------
+ Noto Sans CJK SC （简体中文）
+ Noto Sans CJK TC （繁体中文）
+ Noto Sans CJK KR （韩文）
+ Noto Sans CJK JP （日文）

中文-思源宋体
+ Noto Serif CJK SC （简体中文）
+ Noto Serif CJK TC （繁体中文）
+ Noto Serif CJK KR （韩文）
+ Noto Serif CJK JP （日文）

```bash
# 常用字体打包 - hinted
ls -d hinted/NotoSans-* hinted/NotoSerif-* hinted/NotoSansUI-* hinted/NotoSansCJKsc-* hinted/NotoSerifCJKsc-* hinted/NotoMono-* hinted/NotoSansMonoCJKsc-* unhinted/NotoEmoji-* unhinted/NotoColorEmoji* | grep -v "\\.zip" | zip -@ Noto-hinted.zip;

# 常用字体打包 - unhinted
ls -d unhinted/NotoSans-* unhinted/NotoSerif-* unhinted/NotoSansUI-* hinted/NotoSansCJKsc-* hinted/NotoSerifCJKsc-* hinted/NotoMono-* hinted/NotoSansMonoCJKsc-* unhinted/NotoEmoji-* unhinted/NotoColorEmoji* | grep -v "\\.zip" | zip -@ Noto-unhinted.zip;
```