import os
# 由于XPath属于lxml库模块，所以首先要安装库lxml pip install lxml
from lxml import etree
import requests

# 唐诗
if not os.path.exists('./古诗'):
    os.mkdir('./古诗')


def gethushi(url, headers):
    requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接

    proxies = {"http": None, "https": None}  # 在这里由于公司有代理。在这里要关闭代理
    page_text = requests.get(url=url, headers=headers,proxies=proxies, timeout=300)  #timeOut 是设置超时时间。
    page_text.encoding = 'utf-8'# 将得到的数据进行编码
    return page_text.text  # 将得到的结果转为文本

# 解析根据诗文的题目，去解析到古诗的详细地址
def get_title(res):
    parse = etree.HTML(res)
    # print(html) #<Element html at 0x25be0d7adc8>
    AllItem = []
    # 使用xpath匹配文章标签xpath()返回为一列表  @修饰属性  /text() 获取当前路径下的文本内容
    url = parse.xpath('//*[@id="html"]/body/div[2]/div[1]//@href')
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    return url


# 地址的处理，将古诗的url进行处理。在这里就相当于深度遍历策略
def urldeal(url):
    urls = []
    for i in url:
        i = "https://so.gushiwen.cn" + i
        urls.append(i) #字符串的添加到数组中
    return urls # 将处理后的结果进行返回


# 遍历细节
def bianlixpath(la):

    #异常处理，防止程序挂掉
    try:
        return la[0]  # 去第一个
    except IndexError:
        return "出现异常！"
    else:

        return la[0]



# 获取urls的文章
def proms(urls, heards):
    fp = open("古诗/诗句初选/乐府.txt", 'w', encoding='utf-8')  # 写入文件

    for i in urls:
        page_text = gethushi(i, heards) # 调用之前定义的方法

        parse = etree.HTML(page_text) # 开始解析
        # print(html) #<Element html at 0x25be0d7adc8>

        # 使用xpath匹配文章标签xpath()返回为一列表  @修饰属性  /text() 获取当前路径下的文本内容
        title = parse.xpath('//*[@id="sonsyuanwen"]/div[1]/h1/text()')  #使用xpath进行解析
        title = bianlixpath(title) # 得到古诗的名
        #    print(title)
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        auther = parse.xpath('//*[@id="sonsyuanwen"]/div[1]/p/a/text()') # 的到作者信息
        auther = bianlixpath(auther)

        detail = parse.xpath('/html/body/div[2]/div[1]/div[2]/div[1]//div[2]//text()') # 解析古诗文
        for i in detail:
            d = i
            fp.write(d + "\n") # 将数据写入到文件

        print(title + "load---->secces!") # 下载结束提示。

    print("seccees!")
    fp.close()# 关闭文件

# 程序启动的入口
if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/gushi/yuefu.aspx'
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"

    }




    res = gethushi(url, headers)
    gushiurl = get_title(res)

    urls = urldeal(gushiurl)
    proms(urls, headers)
