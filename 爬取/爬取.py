# -*- coding:utf-8 -*-

"""
    爬取网易云音乐热歌榜的最新评论，指定页数的所有评论，比如前10页
    2018年6月26日

"""

import os
import re
import random
import urllib.request
import urllib.error
import urllib.parse
from Crypto.Cipher import AES
import base64
import requests
import json
import time


agents = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

headers = {
    'Host':'music.163.com',
    'Origin':'https://music.163.com',   #源
    'Referer':'https://music.163.com/song?id=28793052',#防盗链
    'User-Agent':''.join(random.sample(agents, 1))
}

# 除了第一个参数，其他参数为固定参数，可以直接套用
# offset的取值为:(评论页数-1)*20,total第一页为true，其余页为false
# 第一个参数
# first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
# 第二个参数
second_param = "010001"
# 第三个参数
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# 第四个参数
forth_param = "0CoJUm6Qyw8W8jud"


# 获取参数
def get_params(page):  # page为传入页数
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    if(page == 1):  # 如果为第一页
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
        h_encText = AES_encrypt(first_param, first_key, iv)
    else:
        offset = str((page-1)*20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset,'false')
        h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


# 获取 encSecKey
def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


# 解密过程
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    encrypt_text = str(encrypt_text, encoding="utf-8")  # 注意一定要加上这一句，没有这一句则出现错误
    return encrypt_text


# 获得评论json数据
def get_json(url, params, encSecKey):
    data = {
         "params": params,
         "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content.decode('utf-8')  # 解码


# 获取热歌榜所有歌曲名称和id
def get_all_hotSong():
    url = 'http://music.163.com/discover/toplist?id=3778678'    # 网易云云音乐热歌榜url
    header = {'User-Agent': ''.join(random.sample(agents, 1))}  # random.sample() 的值是列表, ''.join()转列表为字符串
    request = urllib.request.Request(url=url, headers=header)
    html = urllib.request.urlopen(request).read().decode('utf8')   # 打开url
    html = str(html)     # 转换成str
    # print(html)
    pat1 = r'<ul class="f-hide"><li><a href="/song\?id=\d*?">.*</a></li></ul>'  # 进行第一次筛选的正则表达式
    result = re.compile(pat1).findall(html)     # 用正则表达式进行筛选
    # print(result)
    result = result[0]     # 获取tuple的第一个元素

    pat2 = r'<li><a href="/song\?id=\d*?">(.*?)</a></li>'  # 进行歌名筛选的正则表达式
    pat3 = r'<li><a href="/song\?id=(\d*?)">.*?</a></li>'   # 进行歌ID筛选的正则表达式
    hot_song_name = re.compile(pat2).findall(result)     # 获取所有热门歌曲名称
    hot_song_id = re.compile(pat3).findall(result)     # 获取所有热门歌曲对应的Id
    # print(hot_song_name)
    # print(hot_song_id)

    return hot_song_name, hot_song_id


# 抓取某一首歌的前page页评论
def get_all_comments(hot_song_id, page, hot_song_name, hot_song_order):  # hot_song_order为了给文件命名添加一个编号
    all_comments_list = []  # 存放所有评论
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + hot_song_id + '?csrf_token='   # 歌评url

    dir = os.getcwd() + '\\Commen\\'
    if not os.path.exists(dir):     # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(dir)

    num = 0
    f = open(dir + str(hot_song_order) + ' ' + hot_song_name + '.txt', 'w', encoding='utf-8')
    # ' '是为了防止文件名也是数字混合，加个空格分隔符，写入文件, a 追加

    for i in range(page):  # 逐页抓取
        # print(url, i)
        params = get_params(i+1)
        encSecKey = get_encSecKey()
        json_text = get_json(url, params, encSecKey)
        # print(json_text)

        json_dict = json.loads(json_text)
        for item in json_dict['comments']:
            comment = item['content']  # 评论内容
            num += 1
            f.write(str(num) + '.' + comment + '\n')
            comment_info = str(comment)
            all_comments_list.append(comment_info)
        print('第%d首歌的%d页抓取完毕!' % (hot_song_order, i+1))
        # time.sleep(random.choice(range(1, 3)))   # 爬取过快的话，设置休眠时间，跑慢点，减轻服务器负担
    f.close()
    # print(all_comments_list)
    # print(len(all_comments_list))
    return all_comments_list


if __name__ == '__main__':
    start_time = time.time()  # 开始时间

    hot_song_name, hot_song_id = get_all_hotSong()

    num = 0
    while num < len(hot_song_name):    # 保存所有热歌榜中的热评
        print('正在抓取第%d首歌曲热评...' % (num+1))
        # 热门歌曲评论很多，每首爬取最新的10页评论
        get_all_comments(hot_song_id[num], 10, hot_song_name[num], num+1)
        print('第%d首歌曲热评抓取成功' % (num+1))
        num += 1

    end_time = time.time()  # 结束时间
    print('程序耗时%f秒.' % (end_time - start_time))
