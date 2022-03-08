fp=open("./数据/text02.txt","w",encoding="utf-8")
tp=open("./数据/text01.txt","r",encoding="utf-8")
list=tp.readlines()
for line in list:
    if line == '\n':
        line = line.strip("\n")
    fp.write(line)
print("cccc")



