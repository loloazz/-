# -*- coding:utf-8 -*-
import requests
# 由于XPath属于lxml库模块，所以首先要安装库lxml pip install lxml
from lxml import etree
import csv

url = "https://news.sina.com.cn/china/  "# 爬取页面url地址

# 根据url获取页面源码
def get_html(url):
    response = requests.get(url)
    response.encoding ='utf-8'
    return response.text

# 获取指定标签的内容
def getAllItem(res):
    #  #将字符串解析为html文档 HTML  可以自动补全 li标签  body和html标签
    html = etree.HTML(res)
    # print(html) #<Element html at 0x25be0d7adc8>
    AllItem = []

    # 使用xpath匹配文章标签xpath()返回为一列表  @修饰属性  /text() 获取当前路径下的文本内容
    title = html.xpath('//ul[@class="news-2"]/li/a/text()')
    url = html.xpath('//ul[@class="news-2"]/li/a/@href')
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    for index ,i in enumerate(title):
        Items = {}
        Items['title'] = i
        Items['url'] = url[index]
        AllItem.append(Items)
    return AllItem

# 加爬取结果写入文件
def writecsv(AllItem):
    # 打开文件，追加a
    with open('text.csv' ,'a', newline='') as out:
        # 设定写入模式 dialect就是定义一下文件的类型，我们定义为excel类型
        csv_write = csv.writer(out ,dialect='excel')
        # 写入具体内容
        # 先写入columns_name
        csv_write.writerow(["序号" ,"title" ,"url"])
        for index ,i in enumerate(AllItem):
            csv_write.writerow([index +1 ,i['title'] ,i['url']])
    return True

# 读取csv文件内容
def readercsv():
    with open("text.csv" ,"r") as csvfile:
        reader = csv.reader(csvfile)
        # 这里不需要readlines
        for line in reader:
            print(line)



    res = get_html(url)
    AllItem = []
    AllItem = getAllItem(res)
    writecsv(AllItem)
    readercsv()

