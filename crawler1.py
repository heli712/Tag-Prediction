import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
tags=[]
final=[]
for i in range(2,13):
    res = requests.get("https://stackoverflow.com/tags?page="+str(i)+"&tab=popular")
    soup = BeautifulSoup(res.text,"html.parser")
    tag=soup.select(".post-tag")
    for i in range(36):
        tags.append(str(tag[i]))
        tags=tags[0].split(">")
        tags=tags[1].split("<")
        final.append(tags[0])
        tags=[]
for x in final:
    for i in range(500):
        try:
            res = requests.get("http://stackoverflow.com/questions/tagged/"+x+"?tab=newest&page="+str(i)+"&pagesize=15")
            soup = BeautifulSoup(res.text,"html.parser")
            question=soup.select(".question-summary")
            f = open(""+x+".txt", "a")
            for que in question:
                q=que.select_one(".question-hyperlink").getText()
                print(len(q))
                f.write(q+"\n")
        except Exception:
            pass
