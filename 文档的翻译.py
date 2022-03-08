#通过百度翻译来
import os
# 由于XPath属于lxml库模块，所以首先要安装库lxml pip install lxml
from lxml import etree
import requests

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
}


def translate(url):
    page_text=requests.get(url,headers).text
    parse = etree.HTML(page_text)
    list=parse.xpath('/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]/span/text()')
    return list


def bianli(list):
    return  list[0]

def urldeal(list):
    list2 =[]
    j=0
    for i in list:
        list2[j] = "https://fanyi.baidu.com/?aldtype=16047#zh/en/"+i
        j+=1
    return list2

def filedeal(rname1,wname2):
    fp=open(wname2,"w",encoding="utf-8")
    tp=open(rname1,"r",encoding="utf-8")
    list=tp.readlines()
    list2=urldeal(list)
    for i in list2:
        translateList = translate(i)
        deal = bianli(translateList)
        fp.write(deal)
        print(deal)



if __name__ == '__main__':
    filedeal("./数据/中文对答数据集","./数据/翻译后.txt")
    print("翻译成功")