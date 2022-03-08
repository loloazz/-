tp=open('F:\数据的爬取\英语语料爬取\合并后英文数据.txt', 'r', encoding="utf-8")
fp=open('F:\数据的爬取\英语语料爬取\英语数据处理后\英文1.txt','w',encoding="utf-8")
lp=open('F:\数据的爬取\英语语料爬取\英语数据处理后\英文2.txt','w',encoding="utf-8")

list=tp.readlines()
for i in list:
    str=i.split(" *** ",1)[0]
    fp.write(str+"\n")
    str1=i.split(" *** ",1)[1]
    lp.write(str1)

fp.close()
lp.close()
tp.close()
