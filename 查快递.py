#-*-coding:utf-8-*-
import urllib
import json
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def gettype(number):#定义取快递类型函数
    def getlist():#取快递类型列表
        req = urllib.urlopen('http://www.kuaidi100.com/autonumber/autoComNum?text=%d' %number)
        html = req.read()
        dict_html = json.loads(html)
        return dict_html['auto']
    for i in getlist():
        type = i['comCode']
    return type    

def getprocess(url):#定义获取快递进度函数
    req = urllib.urlopen(url)
    html =  req.read()
    #type = sys.getfilesystemencoding()          #取文件系统编码类型
    #html = html.decode('utf-8').encode(type)    #utf-8解码  由于解码后和json里面解码冲突，故注释掉此段代码
    dict_info =json.loads(html)
    return dict_info['data']



number= input(u"请输入快递单号：")

type = gettype(number)#获取快递类型


Address = 'http://www.kuaidi100.com/query?type=%s&postid=%d&id=1&valicode=&temp=0.33020057185034335' %(type,number)
for i in getprocess(Address):
    print i['ftime'] + i['context']
