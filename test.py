import requests # 导入请求requsets的包

url= 'http://www.baidu.com' # 待爬取的源目的地址
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
} # 请求头信息

response=requests.get(url, headers) # 发送请求
response.encoding='UTF-8' # 设置编码
print(response.text) # 转成文本格式并打印