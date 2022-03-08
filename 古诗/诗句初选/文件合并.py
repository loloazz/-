#coding=utf-8
import os
# 目标文件夹的路径
filedir ="F:\数据的爬取\古诗\完成"
#获取目标文件的文件名称列表
filenames=os.listdir(filedir)
#打开一个新文件，如果没有则创建
f=open("F:\数据的爬取\古诗\完成\hebin.txt", 'w+', encoding='utf8')

#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath,encoding='utf8'):
        f.writelines(line)
    f.write('\n')
#关闭文件
f.close()
