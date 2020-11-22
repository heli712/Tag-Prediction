import os
arr=os.listdir()
for x in arr:
    if x!="copy.py":
        f=open(x,"r")
        f2=open("all.txt","a")
        for i in f:
            i=i.rstrip()
            f2.write(i+"\n")
