# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-27 09:49:44
# @Author  : HannochTao (hannochtao@163.com)
# @Link    : http://www.imstudy.online
# @Version : 1.4

import requests
from Translate.calcTk import Py4Js
from bs4 import BeautifulSoup
import re

__goolelanguage__ = {'英语': 'en', '中文': 'zh-CN', '日语': 'ja', 'auto': 'en'}


def google_translate(text: object = '', to_language: object = '') -> object:
    """
    :param text: type content
    :param to: auto Chinese
    :return: translate result
    """
    js = Py4Js()
    tk = js.getTk(text)

    header = {'content-type': 'application/json',
              'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    # 要访问的url类似如下试例，把下面的url分割
    """
    https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=ja&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld
    &dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0
    &tsel=0&kc=1&tk=440454.52746&q=%E6%88%91%E6%98%AF%E4%B8%AD%E5%9B%BD%E4%BA%BA
    """
    url_one = "http://translate.google.cn/translate_a/single?client=t&sl="
    sl = 'auto'
    tl = '&tl=' + __goolelanguage__[to_language]
    url_two = "&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2&tk="
    token = tk
    q = '&q=' + text
    # 把参数拼接成url
    url = url_one + sl + tl + url_two + token + q
    # print(url)
    response = requests.get(url, headers=header)

    # print(response.text)
    # 解析网页得到翻译结果
    try:
        soup = BeautifulSoup(response.content, 'lxml')
        # print(str(soup))
        tra_result = re.findall('\[\"(.*?)\"\,\"', str(soup))
        str_tra_result = ''.join(tra_result)
        result = str_tra_result.replace(r'\n', '\n')
        return result
        #print(result)
    except:
        print("Translation Failed!")


