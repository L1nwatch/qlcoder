# Python 编程练习

弟弟学习 Python 没啥入门的练习, 直接做项目估计搞不来, 还是一点一点练吧, 通过测试来检验是否代码敲对了

另外顺便作为自己千里码练习的地方了...

* 题目来源:
    * [千里码](http://www.qlcoder.com/explore)
    * [挑战 Python](http://www.pythontip.com/coding/code_oj)
    * 全国计算机等级考试二级 C 语言

## 题目清单
* 千里码
    * 题目 1 -【第**2333**个能被**2或者被3整除**的正整数是多少?】
    * 题目 -【自由之门】，翻墙一下子就有了： `https://en.wikipedia.org/wiki/Great_Wall_of_China`
    * 题目 -【English】，读起来没啥压力：`to learn more English`
    * 题目 -【Get&Post】，比起用 js，自己还是比较喜欢用 Python 解决，手动提交一下，把 cookie 拿下来后用 requests 库 POST 掉，详看对应文件夹下的 `solve.py`
    * 题目 -【我要建站-1】，自己有个 VPS，放个 html，里面只写自己的用户名，然后过了
    * 题目 -【彩虹】，mac 自带的工具：数码测色计，选择【显示原生值】，得到 16 进制数后转换一下就可以了
    * 题目 -【访客统计】，Python 脚本加正则解决了
    * 题目 -【IP】，ping 一下就得到 IP 地址了
    * 题目 -【Cookie】，chrome 的开发者工具, 检查一下页面 7530, 发现了一个 cookie 存在 Url 编码, 解码一下, 得到一串字符, 其实答案就 4 个字符...还以为要解密那一堆, 不过发现每次刷新都不一样果断知道答案了
    * 题目 -【数据脱敏】，把 md5 放在 [Hash Toolkit](http://hashtoolkit.com/) 一下子就出来了
    * 题目 -【Basic CSS】，幸好看了讨论区，是 div1 里的第一个框改为 `32px 161px`，div2 里的第二个框改为 `49px 40px`
    * 题目 - 【跑马灯】，看了讨论区，找到 `lottery.marquee.js`，把 `alert(de.toString(CryptoJS.enc.Utf8));` 前的 if 去掉就行，注意在 chrome 下改完得按 `cmd+s(macOS)` 保存，界面会变红，这样才能生效
    * 题目 - 【商品数量-1】，用 Python 脚本解决了，幸好数量不多，初始化为 1000 了
    * 题目 - 【商品数量-2】，用 Python，同样的脚本，慢了许多，最后迫不得已用 gmpy2 库加速了一下，还是挺久，几分钟内能跑出来
    * 题目 - 【热点营销-1】，用 Python 脚本, 参考讨论区学习了图论, 很不错
    * 题目 - 【热点营销-2】，同用 Python 脚本, 参考讨论区, 知道了在上一题的基础上还要再考虑孤立结点
    * 题目 - 【断点续传】，用 Python 脚本， 参考学长的文章知道了有这么一个 `Range: bytes=0-20` 的 HTTP 头，剩下的就是 requests 的事情了
    * 题目 - 【我从哪里来】，自己是用 Chrome 的插件【modify-http-headers】实现修改 HTTP 头的 Referer 字段，后来看评论区推荐了神器 Fiddler，虽然没试
    * 题目 - 【以图搜图-1】，直接上[谷歌识图](https://www.google.com/imghp?hl=zh-CN)
    * 题目 - 【文件管理】，用 Python 脚本遍历一下文件夹即可
    * 题目 - 【Git】，Fork 一下，直接在 GitHub 上编辑 readme，然后保存到自己 fork 的分支后，再在 GitHub 页面上 Pull Request
    * 题目 - 【豆瓣评分爬取】，用 Python 脚本过了，注意是爬取前 166 部，用的 requests + bs4 库
    * 题目 - 【Robots协议】，用 chrome 插件改下 HTTP 头就可以了
    * 题目 - 【老王装货】，用 Python 脚本过了, 学习了一下背包问题
    * 题目 - 【动态爬虫】，用 Python 脚本找出了后面几个网页的排序, 至于 1 和 2 和 10 频率太接近了, 所以这三个是猜的, 最后对了
* 挑战 Python
    * 题目 2 - 【列表排序/字符串逆序/打印字典键】
    * 题目 3 - 【字符串奇数位打印/素数判定/求矩形面积和周长】
    * 题目 4 - 【求解素数/求中位数/小写转换】
    * 题目 5 - 【最大公约数/最小公倍数/大写转换】
    * 题目 6 - 【判断公约数/求公约数个数/打印矩阵】
    * 题目 7 - 【提取数字的每一位/科学计数法表示每一位/2 进制转换】
    * 题目 8 - 【统计单词个数/计算平均值并返回大于平均值的数/计算公式的结果】
    * 题目 9 - 【计算平均值并返回小于平均值且最接近平均值的数/计算公式的结果/矩阵右上半三角元素翻倍】
    * 题目 10 - 【计算平均值以及前移大于平均值的数/首字母大写转换/计算周边元素平均值】
    * 题目 11 - 【计算平均值以及前移大于平均值的数/统计元音字母个数/计算周边元素之和】
    * 题目 12 - 【字符串面值的整数求和/统计大小写字母格式/保留小数位数】
    * 题目 13 - 【产生随机列表/读入矩阵并输出对角线之和/实现矩阵转置】
    * 题目 14 - 【找出矩阵每列最大值/交换变量值/求素数/构造矩阵】
    * 题目 15 - 【进制数转换/找出最长字符串/判断幻方/计算公式】
    * 题目 16 - 【删除空格/回文数判定/二维转一维/数字字符前移】
    * 题目 17 - 【字符串交叉拼接/删除字符串指定字符/矩阵行交换】
    * 题目 18 - 【ASCII 升值排序字符串/字符串奇数位大小写转换/矩阵列左移】
    * 题目 19 - 【按规律生成矩阵/合并整数/矩阵找数】