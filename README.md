# xxqg
学习强国自动化答题测试

所需要库：uiatuomator2，PIL，aircv，aip（百度提供的图片识别api），requests（用于更新题库）

Model.py:封装了各类函数
其中do_image函数调用百度的接口，如有需要请自行注册（https://ai.baidu.com/tech/ocr/general）免费

function1.py:挑战答题模块
1.ui2并未提供.xpath的随机点击，为了防止固定点点击被检测，采用图片像素匹配随机定位，所以未适配所有分辨率，默认1080×2400，如需要请手调get_xp()函数
2.该功能并未优化，对于答案较长的文本只能默认出错，通过check函数循环检测直至完成（出现这种情况概率很低，但并不是没有）

function4.py:争上游/双人答题模块

function3.py:视听学习模块

robots.py:题库生成模块
1.该模块同样需要百度的接口
2.所爬取的网站没有robots协议
