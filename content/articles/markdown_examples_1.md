Title: Markdown Examples Part 1
Author: Hython
Date: 2019-01-02 12:00
Category: blogging
Tags: markdown

Basic markdown examples are shown below

This text is **bold**
This text is also __bold__

This text is *italic*
This text is also _italic_

This text is **_italic and bold_**

# An h1 heading
## An h2 heading
### An h3 heading...
###### An h6 heading

A list with numbers:
1. One
2. Two
3. Three

A list with bullets:
* Bullet
* Bullet
* Bullet

Here's a blockquote:

> Simple is better than complex

Here's a table:

| Column1 | Column 2 | Column 3 |
|---|---|---|
| Value 1 | Value 2 | Value 3 |
| Value 4 | Value 5 | Value 6 |
| Value 7 | Value 8 | Value 9 |
  
  
Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
  
  
    :::javascript
    var s = "JavaScript syntax highlighting";
    alert(s);

    :::python3
    s = "Python syntax highlighting"
    print s

    :::html
    No language indicated, so no syntax highlighting. 
    But let's throw in a <b>tag</b>.

    :::
    # 输入宽度: 30
    ------------------------------
    商 品                     价 格
    ······························
    面  粉                    6.50
    韭  菜                    3.50
    鸡  蛋                    10.00
    虾  仁                    18.60
    酱  油                    12.00
    ------------------------------

多行公式：

    :::math
    \displaystyle
    \left( \sum\_{k=1}^n a\_k b\_k \right)^2
    \leq
    \left( \sum\_{k=1}^n a\_k^2 \right)
    \left( \sum\_{k=1}^n b\_k^2 \right)


    :::katex
    \displaystyle 
        \frac{1}{
            \Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{
            \frac25 \pi}} = 1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {
            1+\frac{e^{-6\pi}}
            {1+\frac{e^{-8\pi}}
             {1+\cdots} }
            } 
        }


    :::latex
    f(x) = \int_{-\infty}^\infty
        \hat f(\xi)\,e^{2 \pi i \xi x}
        \,d\xi
