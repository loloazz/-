import os
# 由于XPath属于lxml库模块，所以首先要安装库lxml pip install lxml
from lxml import etree
import requests
#唐诗
if not os.path.exists('./古诗'):
    os.mkdir('./古诗')



def gethushi(url,headers):
  page_text = requests.get(url=url, headers=headers)
  page_text.encoding='utf-8'
  return page_text.text



def get_title(res):

    parse=etree.HTML(res)
    # print(html) #<Element html at 0x25be0d7adc8>
    AllItem = []
    # 使用xpath匹配文章标签xpath()返回为一列表  @修饰属性  /text() 获取当前路径下的文本内容
    url = parse.xpath('//*[@id="html"]/body/div[2]/div[1]//@href')
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    return url

#地址的处理
def urldeal(url):
    urls=[]
    for i in url:
       i="https://so.gushiwen.cn"+i
       urls.append(i)
    return urls



#遍历细节
def bianlixpath(la):
    return la[0]


#获取urls的文章
def proms(urls,heards):
    fp = open("古诗/诗句初选/唐诗三百.txt", 'w', encoding='utf-8')

    for i in urls:
            page_text=gethushi(i,heards)


            parse = etree.HTML(page_text)
            # print(html) #<Element html at 0x25be0d7adc8>

            # 使用xpath匹配文章标签xpath()返回为一列表  @修饰属性  /text() 获取当前路径下的文本内容
            title = parse.xpath('//*[@id="sonsyuanwen"]/div[1]/h1/text()')
            title=bianlixpath(title)
        #    print(title)
            # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
            auther = parse.xpath('//*[@id="sonsyuanwen"]/div[1]/p/a/text()')
            auther=bianlixpath(auther)
            detail = parse.xpath('/html/body/div[2]/div[1]/div[2]/div[1]//div[2]//text()')
            for i in detail:
                d=i
                fp.write(d+"\n")

           # print(detail)


    print("seccees!")
    fp.close()




if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/gushi/tangshi.aspx'
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    res=gethushi(url,headers)
    gushiurl =get_title(res)

    urls=urldeal(gushiurl)
    proms(urls,headers)









