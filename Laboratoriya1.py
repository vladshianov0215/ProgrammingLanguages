import requests
import re

findedEmails = [] 
resultEmails = []
URLnotLooked =[] 
URLlooked = [] 

findedUrl = []
startURL = 'http://www.mosigra.ru'

URLnotLooked.append(startURL)
n=0
print("подождите 10 итераций")

def go(s,n):
    
    if(s<n):
   
        sitecode = requests.get(URLnotLooked[0])
        URLlooked.append(URLnotLooked[0])
        URLnotLooked.pop(0) 
   
        findedEmails = re.findall(r'[\w[\w\_\.]+\@[\w\_\-]+\.[\w\_\-\/]+',sitecode.text)
        for i in range(len(findedEmails)): 
            if findedEmails[i] not in resultEmails:
                resultEmails.append(findedEmails[i])

        findedUrl = re.findall(r'href="(http://www.mosigra.ru\/[\w\_\-\/\.]+)',sitecode.text)
        for i in range(len(findedUrl)):
            if findedUrl[i] not in URLnotLooked and findedUrl[i] not in URLlooked:
                URLnotLooked.append(findedUrl[i])
        s=s+1    
        print(s)
        go(s,n)
    
go(0,10)

print("Поиск закончен!")
print("") 
for i in range(len(resultEmails)):
    print (resultEmails[i])
