Title: 语法拾遗1：python文本字符串格式化输出总结
Author: hython
Date: 2018-05-30 00:05
Modified: 2018-06-01 21:05
Category: Python
Tags: Python
Slug: python-string-format


本文主要总结了`format`格式化输出文本的用法。


1. 替换字段使用`{}`括起来，如果需要输出结果包含`{}`则应使用{% raw %}`{{}}`{% endraw %}双花括号转义。


    ```
    In [1]: "{{test's string}}".format()
    Out[1]: "{test's string}"
    ```

2. 使用未命名字段名替换和指定参数替换

    一般用法既可以使用未命名字段也可以指定参数，两种可单独使用也能混用，但是注意不能同时使用手动指定编号和自动编号：
    混合使用法举例


    :::
    In [5]: "{foo} {} {bar} {}".format(2, 4, foo=1, bar=3)
    Out[5]: '1 2 3 4'
    
    # 通过索引指定时可以不管参数的顺序
    In [6]: "{foo} {1} {bar} {0}".format(4, 2, foo=1, bar=3)
    Out[6]: '1 2 3 4'
    
    # 还可以使用引用
    In [8]: import math
    In [9]: tmp = "模块{mod.__name__}中的圆周率π的默认值为{mod.pi}"
    In [10]: tmp.format(mod=math)
    Out[10]: '模块math中的圆周率π的默认值为3.141592653589793'


3. 基本转换标识符的使用

    - 三个标志`s`、`r`和`a`分别是指使用`str`、`repr`和`ascii`进行转换叹号`!`之前的字符串：


    
    In [15]: "{str!s} {str!r} {str!a}".format(str="π")
    Out[15]: "π 'π' '\\u03c0'"


    - 格式说明符冒号`:`的使用，一般其后跟类型说明符。比如表示定点数的`f`以及表示二进制的`b`。


    
    # 浮点小数格式
    In [22]: "The number is {:f}".format(2018)
    Out[22]: 'The number is 2018.000000'
    # 二进制格式
    In [23]: "The number is {:b}".format(2018)
    Out[23]: 'The number is 11111100010'

    - 其他的格式表示类型如下表：

        | 类型 | 代表格式 |
        | --- | --- |
        | b | 用二进制表示整数 |
        | c | 解读整数为Unicode码 |
        | d | 十进制整数 |
        | e | 科学计数表示法 |
        | E | 同`e`，可表示指数 |
        | f | 指定位数的小数表示 |
        | F | 同`f`，对特殊值`inf`和`nan`使用大写表示 |
        | g | 自动选择表示为小数或科学计数，小数时至少一位 |
        | G | 同`g`，但使用大写表示指数和特殊值 |
        | n | 同`g`，但跟随地区区域显示位数分隔符 |
        | o | 整数表示为八进制 |
        | s | 默认，表示文本字符串 |
        | x | 十六进制，其中使用小写字母 |
        | X | 同`x`, 其中使用大写字母 |
        | % | 表示为百分比 |

    - `:`后面用整数表示宽度和精度，需注意数字和文本的对齐位置不同，表示精度时前面要加小数点`.`：


    :::python3
    # 宽度
    In [24]: "{:10}".format(2)
    Out[24]: '         2'

    In [25]: "{:10}".format("2")
    Out[25]: '2         '

    # 精度
    In [30]: "{:.2f}".format(math.pi)
    Out[30]: '3.14'

    # 宽度加精度
    In [31]: "{:10.5}".format(math.pi)
    Out[31]: '    3.1416'
    
    - `:`后面跟`,`逗号表示插入千位数分隔符（跟随地区格式）


     In [37]: '先挣他一个{:,}'.format(10**10)
     Out[37]: '先挣他一个10,000,000,000'
         

    - 指定左对齐、右对齐和居中，可在`:`后分别使用`<`、`>`和`^`:
    
        ![三种对齐格式](https://upload-images.jianshu.io/upload_images/383-9b29f512da63f067.jpg)
    
    
    # :冒号后可接填充符，0则为用0填充
    In [40]: "{:w^12}".format(" site ")
    Out[40]: 'www site www'
    In [41]: "{:0<10}".format(1234)
    Out[41]: '1234000000'


4. 在对齐符合后也可使用`+`,`=`,`#`等分别表示在字符前显示正号，分离符号和文本，以及用不同进制显示，由于不常用在此不做介绍。

    ##### 综合运用案例：根据指定的宽度打印格式化购物小票


    :::python3
    width = int(input('输入宽度: '))
    
    price_width = 10
    item_width = width - price_width
    
    header_tmpl = "{{:{}}}{{:>{}}}".format(item_width, price_width)
    tmpl = "{{:{}}}{{:>{}.2f}}".format(item_width, price_width)
    
    print('-' * width)
    
    print(header_tmpl.format('商 品', '价 格'))
    
    print('·' * width)
    
    print(tmpl.format('面  粉', 6.5))
    print(tmpl.format('韭  菜', 3.5))
    print(tmpl.format('鸡  蛋', 10.0))
    print(tmpl.format('虾  仁', 18.6))
    print(tmpl.format('酱  油', 12))
    
    print('-' * width)


最终显示结果为：

    :::bash
    输入宽度: 30
    ------------------------------
    商 品                     价 格
    ······························
    面  粉                    6.50
    韭  菜                    3.50
    鸡  蛋                    10.00
    虾  仁                    18.60
    酱  油                    12.00
    ------------------------------

怎么样，这盘三鲜饺够味不。

> 以上部分内容参考自《python编程基础第三版》，感谢阅读，如果有遗漏欢迎留言补充。
