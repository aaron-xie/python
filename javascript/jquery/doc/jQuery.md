[TOC]

#jQuery

##了解jQuery
JQuery是一个兼容多浏览器的javascript类库，核心理念是write less,do more(写得更少,做得更多)。是一个快速的简洁的javascript框架，可以简化查询DOM对象、处理事件、制作动画、处理Ajax交互过程。在2006年1月由美国人John Resig在纽约的barcamp发布。

![John Resig](img/zz.jpg "jQuery作者John Resig")
作者：John Resig
官方网站：http://jquery.com/

###jQuery版本
* 1.x.x
    - 兼容低版本浏览器IE8-
    - 代码过于庞杂，性能不高
    - 最新版本1.12
* 2.x.x
    - 已经不支持IE低版本浏览器IE8-
    - 最新版本2.2
* 3.x.x
    - 3.0 版本是从 2.0 版本分支出来的，但由于改动过大，因此更新了主版本号
    - 不支持IE低版本浏览器
    - 性能大幅度提高（推荐使用）

###下载与安装
* 官网下载
http://jquery.com/download/
* CDN
    - https://code.jquery.com/jquery-3.0.0.js
    - https://code.jquery.com/jquery-3.0.0.min.js

###jQuery对象
* jQuery实例属性
    - length: 返回jQuery对象中匹配元素的个数
    - jquery: 当前jquery类库版本号（一般用于判断是否jquery对象）
    - 下标（索引）: DOM节点
* jQuery的别名：$
* 延迟代码执行：jQuery(document).ready(fn)
    - 页面DOM渲染完成时执行，用来替代window.onload;
    - 简写方式:`jQuery(function($){})`;
* 使用jquery编写代码只需两步
1. 选择元素
2. 操作元素


##选择器
>选择页面中的元素，得到jQuery实例对象

* ID选择器$("#save")
* 类选择器$(".class")
* 标签选择器$("div")
* 复合选择器 $("div,span,p.myClass")
* 属性选择器$('[id=box]')
    - $('li[data-index]'):获取有data-index属性的所有元素
    - $('li[data-index^=10]'):data-index属性以10开头的元素
    - $('li[data-index$=10]'):data-index属性以10结尾的元素
* 表单选择器$(':input')
    - :radio      //匹配所有单选按钮
    - :checkbox   //匹配所有复选按钮

    - :selected   //获取已选择的option元素
    - :checked    //匹配所有被选中的元素(复选框、单选框等，select中的option)


* 判断元素是否可见
    :hidden     //匹配所有不可见元素(display:none)，或者type为hidden的元素
    :visible    //匹配所有可见元素
>以上两个选择器配合is()方法通常用于判断，返回布尔值
```
if(box.is(':visible')){
    box.css('display','none');
}
```



###筛选
>利用选择器得到得结果不一定是我们想要得最终结果，有时需要进一步筛选

####筛选方法
* first()/last(): 获取集合中第一个/最后一个元素
* eq(index|-index): 获取第N个元素,n支持负数（表示从后面查找）
* filter(expr|obj|ele|fn): 筛选出与指定表达式匹配的元素集合。这个方法用于缩小匹配* 的范围。用逗号分隔多个表达式
* slice(start,[end]): 选取一个从start到end(不包括end)匹配的子集
* not(expr|ele|fn): 删除与指定表达式匹配的元素

###查找
>利用当前元素的节点关系去查找其他元素

* 查找子元素
    - find(expr|obj|ele): 查找后代元素
    - children([expr]): 取得匹配元素的所有子元素。(原生js:children)

* 查找父级元素
    - parent([expr]): 获取父元素
    - parents([expr]): 取得所有父级元素
    - closest(expr|obj|ele): 从元素本身开始，逐级向上级元素匹配，并返回最先匹配的元素
    - offsetParent(): 返回第一个有定位属性(absolute,relative,fixed)* 的父元素,如果没有定位父级，则返回html元素

* 查找兄弟元素
    - next([expr]): 返回下一个同辈元素
    - prev([expr]): 获取前一个同辈元素
    - nextAll([expr]): 获取当前元素之后所有的同辈元素 
    - prevAll([expr]) 获取当前元素之前所有的同辈元素
    - siblings([expr]) 获取当前元素的所有兄弟元素（除自身以外的所有兄弟元素 = * prevAll + nextAll）

##jQuery动画
###基本动画效果
* 显示隐藏：show()/hide()
    - hide(duration)通过改变元素的高度、宽度、和不透明度，直到这三个属性值到0
    - show(duration)通过改变元素的高度、宽度、和不透明度，直至内容完全可见

* 滑动（通过改变高度）
    - slideDown([speed,callback])：
        1. 显示元素
        2. 不断改变高度，直到样式内设定的值
    - slideUp([speed,callback])：
        1. 不断改变高度，直到0
        2. 隐藏元素
    - slideToggle([speed,callback])
        当元素隐藏时调用slideDown()，当元素显示时调用slideUp()

* 淡入淡出（通过改变不透明度）
    - fadeIn:
        1)显示元素
        2)不断改变透明度直到1
    - fadeOut:
        1)不断改变透明度直到0
        2)隐藏元素
    - fadeToggle([speed,callback])

    - fadeTo([[speed],opacity,[fn]])  不断改变透明度opacity，直到设定的值，并在动画完成后可选地触发一个回调函数。

>PS：jQuery动画由三种预设速度slow,normal,fast（600，400，200）

###自定义动画
* animate (params,[speed],[fn])

---

[案例]
1. 手风琴效果
2. 自动轮播图效果

---


##ajax
###jQuery的ajax方法
* $.ajax(settings)
    - type:请求类型，默认GET
    - url:数据请求地址（API地址）
    - data:发送到服务器的数据对象，格式：{Key:value}。
    - success:请求成功时回调函数。
    - dataType:设定返回数据的格式，json, jsonp, text(默认), html, xml, script
    - async：是否为异步请求，默认true

* $.get(url,[data],[fn],[dataType]) // type:'get'

* $.post(url,[data],[fn],[dataType]) // type:'post'
 
* load(url,[data],[callback]) 载入远程 HTML 文件代码并插入页面中。


[案例]

* 加载html文件

---

##常用jQuery原型对象的方法
>写在jQuery原型对象中的方法，通过jQuery实例调用

* css(attr[,val]): 获取/改变元素style属性（内联样式） 
    - 取值：css(attr),css(['color','text-align']) <==> getComputedStyle[attr]
    - 赋值：css(attr,val),css({attr:val});
* val(v): 获取/设置匹配表单元素的值（等同于原生js中的value属性）
    * 取值：
    `input.val()`
    * 赋值：
    `input.val(v)`
        - v:字符串
        - v:数组（一般用于单选/复选框的勾选）
        - v:函数function(idx,val){ return 值}//函数内部一定要返回值

* html(): （等同于原生js中的innerHTML）
    取值div.html()：取得第一个匹配元素的html内容
    赋值div.html(':')：设置匹配元素的内容
* text(): 取得所有匹配元素的文本内容。
* addClass()/removeClass(): 添加/删除类,支持多个类同时添加或删除
    - toggleClass(): 如果存在（不存在）就删除（添加）类。
    - hasClass('con'): 判断当前元素是否包含con这个类，返回布尔值（不支持多个类进行判断）
* eq(n) 获取第N个jquery对象（元素）,n支持负数（表示从后面查找）
* index():获取当前元素在同辈元素中的索引值
```
$(this).index();
```
* 显示/隐藏 
    - show()：显示元素
    - hide()：隐藏元素
        - 带参数：同时改变width,height,opacity的动画
* is(expr|obj|ele|fn) 根据选择器、DOM元素或 jQuery 对象来检测匹配元素集合，其中如果有一个元素符合这个给定的选择器表达式就返回true。如果没有元素符合，或者表达式无效，都返回false。
* attr(name[,val]) 设置/获取html标签属性
* prop(attr[,val]) 获取/设置DOM节点属性（一般修改布尔类型属性）
    - 获取：获取在匹配的元素集中的第一个元素的属性值。
    - 赋值：给集合中所有元素属性赋值
        + val为函数
        ```
        $(':checkbox').prop('checked',function(idx,oldVal){
            return !oldVal;
        }
        ```
* each(function(idx,ele){}) //用于遍历jquery对象
    - return true;// 跳过当前循环，进入下一个循环（等效原生js中得continue）
    - return false;// 退出整个each循环（等效原生js中得break）

---

[练习]

1. 选项卡
2. jquery实现表单验证
3. 购买商品飞入购物车效果


[作业]

1. 模拟QQ发送消息

