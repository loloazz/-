fp=open('./古诗数据/1改.txt','r',encoding="utf-8")
tp=open('./古诗数据/2改.txt','w',encoding="utf-8")
list=fp.readlines()
for i in list:
    if(i.find(" *** ")):
        tp.write(i)
print("desaea")