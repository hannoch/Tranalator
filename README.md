# Tranalator
----
基于python语言写的文档翻译器，可实现word文档翻译，突破了百度翻译和google翻译只能一次翻译5000个单词的限制。


# 一、使用说明
下载代码后在python3.7环境下运行Fanven.py文件，如图1所示。
![图1](https://upload-images.jianshu.io/upload_images/5451635-112bbe6823a57fbe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
图1

普通翻译：
需要翻译成中文，英文，日文。可选择选择百度或者谷歌进行翻译，如图2所示。
![图2](https://upload-images.jianshu.io/upload_images/5451635-c331e7b03f773af3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
图2

文档翻译：
点击“打开文件”，选择将要翻译的文档，选择目标语言，再选择百度或者谷歌进行翻译，最后可选择保存到word文档，如图3所示。
![image.png](https://upload-images.jianshu.io/upload_images/5451635-7c21b5204b2f2b3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
图3

# 二、安装说明
## 1.获取代码

    git clone https://github.com/hannoch/Tranalator.git

## 2.安装python环境
参考[python安装百度经验][1]，在此不再重复说明。
## 3.安装所需的模块

### docx扩展包
作用：用于打开word文档。
优点:不依赖操作系统,跨平台。

安装:

    pip install python-docx
    
### Beautiful Soup 模块  
Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据
安装：

    pip install beautifulsoup4

### lxml模块
Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快。
安装：

    pip install lxml

### execjs模块
安装：

     pip install PyExecJS
     
### requests模块
安装：

    pip install requests


## 参考文献
[Python读取word文本操作详解][2] 、
[tkinter模块常用参数(python3)][3]、
[Tkinter选择路径功能的实现][4]、
[python-docx][5]、
[破解google翻译API全过程][6]


  [1]: https://jingyan.baidu.com/article/0bc808fc42dfab1bd485b99f.html
  [2]: http://www.jb51.net/article/133405.htm
  [3]: https://www.cnblogs.com/aland-1415/p/6849193.html
  [4]: https://blog.csdn.net/zjiang1994/article/details/53513377
  [5]: https://python-docx.readthedocs.io/en/latest/index.html
  [6]: http://www.cnblogs.com/by-dream/p/6554340.html
