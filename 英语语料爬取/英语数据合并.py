#coding=utf-8
import os
# 目标文件夹的路径
filedir ="F:\数据的爬取\英语语料爬取\英语数据处理后"
#获取目标文件的文件名称列表
filenames=os.listdir(filedir)
#打开一个新文件，如果没有则创建
f=open("F:\数据的爬取\英语语料爬取\合并后英文数据.txt", 'w+', encoding='utf8')
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath,encoding='utf8'):
        print(line)
        f.writelines(line)
    f.write('\n')
#关闭文件
print("--------------")
f.close()
