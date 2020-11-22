import requests
from bs4 import BeautifulSoup
for x in list1:
    for i in range(10):
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
