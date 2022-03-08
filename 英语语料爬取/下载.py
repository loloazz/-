import os
# 由于XPath属于lxml库模块，所以首先要安装库lxml pip install lxml
from lxml import etree
import requests
#唐诗
if not os.path.exists('./英语'):
    os.mkdir('./英语')


headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
}


#https://raw.githubusercontent.com/candlewill/Dialog_Corpus/master/ChatterBot_corpus/data/english/
baseurl='https://raw.githubusercontent.com/candlewill/Dialog_Corpus/master/ChatterBot_corpus/data/english/'
list= [
    'ai.corpus.json',
    'botprofile.corpus.json',
    'drugs.corpus.json',
    'emotion.corpus.json',
    'food.corpus.json',
    'gossip.corpus.json',
    'greetings.corpus.json',
    'history.corpus.json',
    'humor.corpus.json',
    'literature.corpus.json',
    'math_words.json',
    'money.corpus.json',
    'movies.corpus.json',
    'politics.corpus.json',
    'psychology.corpus.json',
    'science.corpus.json',
    'sports.corpus.json',
    'swear_words.csv',
    'trivia.corpus.json'
]
list2 =[]
list3 =[]
j = 0
for i in list:
    h=baseurl+i
    list2.append(h)
    l="./英语/"+i
    list3.append(l)


k=0
for i in list2:
    fp = open(list3[k], 'w', encoding="utf-8")
    fp.write(requests.get(i,headers).text)
    k=k+1
    print("成功")