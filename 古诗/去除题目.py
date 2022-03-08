

tp=open('./诗句初选/诗经.txt', 'r', encoding="utf-8")
fp=open('./古诗数据/1.txt','w',encoding="utf-8")
list=tp.readlines()
list2 =[]
for line in list:
    if (line !='\n'):
        if(len(line)>10):
             list2.append(line)

for i in list2:
    fp.write(i)
print("cccc")
