tp=open('./完成/古诗合并.txt', 'r', encoding="utf-8")
fp=open('../../大赛/古诗合并1.txt','w',encoding="utf-8")
lp=open('../../大赛/古诗合并2.txt','w',encoding="utf-8")

list=tp.readlines()
for i in list:
    str=i.split(" *** ",1)[0]
    fp.write(str+"\n")
    str1=i.split(" *** ",1)[1]
    lp.write(str1)

fp.close()
lp.close()
tp.close()
