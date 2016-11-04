import requests
import re

allFindIP = [] 
sortIP = []
Subnet = [] 

file = open('access.log', 'r')

allFindIP = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',file.read())
for i in range(len(allFindIP)): 
    if allFindIP[i] not in sortIP:
        sortIP.append(allFindIP[i])

for i in range(len(sortIP)): 
    if re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}',sortIP[i]) not in Subnet:
        Subnet.append(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}',sortIP[i]))

for i in range(len(Subnet)):
    print('IP  подсети:',Subnet[i])
    for j in range(len(sortIP)):
        if re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}',sortIP[j]) == Subnet[i]:
            print(sortIP[j])
    print() 
print('Всего: ',i,' IP адрес')
