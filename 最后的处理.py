fp=open("数据/中文对答数据集.txt", "w", encoding="utf-8")
tp=open("./数据/text02.txt","r",encoding="utf-8")
list=tp.readlines()
j=0
for i in list:
    if(j%2==0):
        i=i.replace("\n","")
        fp.write(i+"***")
    else:
        fp.write(i)
    j+=1
print("cccccccsadasd")