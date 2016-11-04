import requests
import re

findedEmails = [] #Все собранные емейлы
resultEmails = [] #Уникальные емейлы
URLnotLooked =[] #Не посещенные ссылки
URLlooked = [] #Посещенные ссылки

findedUrl = [] #Все куски кода с href
startURL = 'http://www.mosigra.ru' #Сайт, который парсим

URLnotLooked.append(startURL)
n=0
print("подождите 10 итераций") 
while n<10:
   
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
    n=n+1    
    print(n) 
    
print("Поиск закончен!")
print("") 
for i in range(len(resultEmails)):
    print (resultEmails[i])
