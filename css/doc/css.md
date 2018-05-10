[TOC]

#CSS样式
层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML等文件样式的计算机语言

##样式编写位置
* 内联样式
    - style属性
* 内部样式
    - style标签
* 外部样式
    - link标签
        + href: css文件路径
        + rel: stylesheet


##选择器
>CSS选择器用于选择你想要的元素,并设置相应样式
格式: 选择器{}

* id选择器
* class选择器
* 标签选择器
* 属性选择器
* 伪类选择器
* 伪元素选择器
* 复合选择器
```css
    #box{}

    .box{}

    a{}

    [type=text]{}

    :hover{}

    div,p{}
```

##css属性与值
>格式: 选择器{属性:值}

### 字体font
* font-size
* font-weight
* font-family
* font-style
    - normal - 文本正常显示
    - italic - 文本斜体显示
    - oblique - 文本倾斜显示

###文本text
* 水平对齐:text-align
* 首行缩进:text-indent
* 字符转换:text-transform
    - none  默认不转换
    - uppercase 所有字符转成大写
    - lowercase 所有字符转成小写
    - capitalize     所有单词首字母大写
* 文本装饰：text-decoration
    * none
    * underline 

### 背景background
* background-color
* background-image

### 盒模型
* 宽高: width/height
* 边框: border
* 内边距: padding
* 外边距: margin

### 定位position
* 相对定位: relative
* 绝对定位: absolute
* 固定定位: fixed