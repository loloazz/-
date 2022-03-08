fp=open("F:\数据的爬取\英语语料爬取\英语数据处理后\part-r-00000","r",encoding="utf-8")#打开文件以只读的形式
tp=open("F:\数据的爬取\英语语料爬取\英语数据处理后\secces","w",encoding="utf-8")#打开一个文件以只写的形式
list=fp.readlines()# 读取文件
for i in list:
    i=i.replace("\t",",")
    tp.write(i)# 写入文件
    print(i)  # 打印效果



