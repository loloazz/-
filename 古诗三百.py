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

#地址的处理。
def urldeal(url):
    urls=[]
    for i in url:
       i="https://so.gushiwen.cn"+i
       urls.append(i)
    return urls

#遍历细节
def bianlixpath(la):
    return la[0]


#获取urls的文章  并下载
def proms(urls,heards):
    fp = open("古诗/诗句初选/古诗三百.txt", 'w', encoding='utf-8')

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
            fp.write(title + " " + auther )
            detail = parse.xpath('/html/body/div[2]/div[1]/div[2]/div[1]//div[2]//text()')
            for i in detail:
                d=i
                fp.write(d+"\n")
            print(title+"load---->secces!")
    print("seccees!")
    fp.close()

if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/gushi/tangshi.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        # 'Cookie': '''HMACCOUNT_BFESS=47117E057C21E206; BDSFRCVID_BFESS=4gIOJexroG0Ry5QD0XbohnKeweKK0gOTDYLEOwXPsp3LGJLVgxwbEG0PtowxpEt-oxHpogKKWmOTH7IF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oI-MfIvDqTrP-trf5DCShUFsLxtOB2Q-XPoO3KJCJDKGQ53i3n-Jh4R---QiWbRM2MbgylRM8P3y0bb2DUA1y4vpKbvfKeTxoUJ2a-3Wqh5mqtnWyb8ebPRiL-r9Qg-falQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD582e5PVKgTa54cbb4o2WbCQH4cP8pcN2b5oQT8w2HoI0TOvQaR3WqvHbb5vOIJTXpOUWfAkXpJvQnJjt2JxaqRC5-nbHl5jDh3Mhn-bK-oJe4ROWTRy0hvcQb6cShP6yfjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT0jfn3aQ5rtKRTffjrnhPF3Ml5bXP6-hnjy3bRNXC5l3IJiSn3dhxRq5PLUyN3MWh3RymJ42-39LPO2hpRjyxv4bnkW-4oxJpOJa5vOQp52HR7WO-JvbURv3Pug3-AfBx5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoC0XtI-2bKvPKITD-tFO5eT22-usfncA2hcHMPoosIJ-2joGQ58R3UR32fn-bKTiaKJjBMbUoqRHXnJi0btQDPvxBf7p55bf3q5TtUJMDP39KMoMqt4byh3yKMniQKj9-pP5WlQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBD53QeaRabK6aKC5bL6rJabC3Mb3VXU6q2bDeQN3Nh6QI3nRv3J7Saqvqfn5oyT3JXp0vWtv4WbbvLT7johRTWqR4ePn6-xonDh83hpJObUQJHCOOaPJO5hvvSn6O3MAbyfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRPfoC_h3j; BAIDUID_BFESS=4DE237EEB96E77B12DD45437BC339801:FG=1; BDUSS_BFESS=BYMWRYU3BWdTZtcExtQnNkfk50djZ2TmUzSHJxWThCV1VaYXZoODIzblNYVTVpSUFBQUFBJCQAAAAAAAAAAAEAAADkXmlYaG91c2Vhc2RkZGRkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANLQJmLS0CZiZ1''',
        'Accept-Language':'zh-CN,zh;q=0.9'

        }


    res=gethushi(url,headers)

    print(res)
    # gushiurl =get_title(res)
    # urls=urldeal(gushiurl)
    # proms(urls,headers)









