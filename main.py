from collections import Counter
import nltk
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle as c
import os
arr = os.listdir()
print(arr)

def save(clf, name):
    with open(name, 'wb') as fp:
        c.dump(clf, fp)
    print ("saved")

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now","How","I","Why","when"]
words=[]
f=open("all.txt","r")
for i in f:
    i=i.rstrip()
    i=i.split(" ")
    for x in i:
        if x in stop_words:
            continue
        else:
            words.append(x)
for i in range(len(words)):
    if not words[i].isalnum():
        words[i]=""
dictionary=Counter(words)
print(len(dictionary))
del dictionary[""]
dictionary=dictionary.most_common(4000)

print(dictionary)
#now construction for sample program for java........for testing....
for x in arr:
    if x != "main.py":
        list2=[]
        for i in arr:
            if i==x:
                continue
            else:
                list2.append(i)
        feature=[]
        heli=[]
        for j in list2:
            f=open(j,"r")
            for lines in f:
                heli.append(0)
                new=[]
                data=[]
                i=lines.rstrip()
                i=lines.split(" ")
                for k in i:
                    new.append(k.lower())
                for entry in dictionary:
                    if entry[0].lower() in new:
                        data.append(new.count(entry[0].lower()))
                    else :
                        data.append(0)
                feature.append(data)

            else:
                break
        print(len(feature),len(heli))

        # constructing for python......... for testing....
        f=open(x,"r")
        for lines in f:
            heli.append(1)
            new=[]
            data=[]
            i=lines.rstrip()
            i=lines.split(" ")
            for j in i:
                new.append(j.lower())
            for entry in dictionary:
                if entry[0].lower() in new:
                    data.append(new.count(entry[0].lower()))
                else :
                    data.append(0)
            feature.append(data)
        print(len(feature),len(heli))
        x_train,x_test,y_train,y_test= tts(feature,python,test_size=0.2)
        clf = LogisticRegression()
        clf.fit(x_train,y_train)
        preds= clf.predict(x_test)
        print(accuracy_score(y_test,preds))
        save(clf,""+x+".mdl")
