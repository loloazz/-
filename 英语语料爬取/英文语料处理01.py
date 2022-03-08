
# 'ai.corpus.json',
# 'botprofile.corpus.json',
# 'emotion.corpus.json',
# 'food.corpus.json',
# 'greetings.corpus.json',
# 'history.corpus.json',
# 'humor.corpus.json',
# 'literature.corpus.json',
# 'math_words.json',
# 'money.corpus.json',
# 'movies.corpus.json',
# 'politics.corpus.json',
# 'psychology.corpus.json',
# 'science.corpus.json',
# 'sports.corpus.json',
# 'trivia.corpus.json'

def fileNameDeal(prefiles,lastfiles):
    for prefile in prefiles:
        prefile='./英语/'+prefile
        dealprefiles.append(prefile)
    for lastfile in lastfiles:
        lastfile='./英语数据处理后/'+lastfile
        deallastfiles.append(lastfile)
    print("文件名处理成功！")





def run(prefile,lastfile):
    fp=open(prefile,"r",encoding="utf-8")
    tp=open(lastfile,"w",encoding="utf-8")
    list=fp.readlines()
    j = 0
    for line in list:
        if line == '\n':
            line = line.strip("\n")
        else:
            line=line.replace(",","")
            line=line.replace('"',"")
            # tp.write(line)
            if (j % 2 == 0):
                line = line.replace("\n", "")
                tp.write(line + " *** ")
            else:
                tp.write(line)
            j += 1
    tp.close()
    fp.close()
    print("文件处理成功")


if __name__ == '__main__':
    prefiles = ['ai.corpus.json',
                'botprofile.corpus.json',
                'emotion.corpus.json',
                'food.corpus.json',
                'greetings.corpus.json',
                'history.corpus.json',
                'humor.corpus.json',
                'literature.corpus.json',
                'money.corpus.json',
                'movies.corpus.json',
                'politics.corpus.json',
                'psychology.corpus.json',
                'science.corpus.json',
                'sports.corpus.json',
                'trivia.corpus.json'
                ]

    lastfiles = ['ai.corpus.txt',
                 'botprofile.corpus.txt',
                 'emotion.corpus.txt',
                 'food.corpus.txt',
                 'greetings.corpus.txt',
                 'history.corpus.txt',
                 'humor.corpus.txt',
                 'literature.corpus.txt',
                 'money.corpus.txt',
                 'movies.corpus.txt',
                 'politics.corpus.txt',
                 'psychology.corpus.txt',
                 'science.corpus.txt',
                 'sports.corpus.txt',
                 'trivia.corpus.txt']

    deallastfiles = []
    dealprefiles = []
    fileNameDeal(prefiles,lastfiles)
    k=0
    for prefile in dealprefiles:
        run(prefile,deallastfiles[k])
        k+=1