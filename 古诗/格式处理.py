fp=open('./完成/hebin.txt','r',encoding="utf-8")
tp=open('完成/古诗合并.txt', 'w', encoding="utf-8")
list=fp.readlines()
for i in list:
  if(i.count("***")==1):
        tp.write(i)


fp.close()
tp.close()