import requests
import json
import time

url = "https://api.meetup.com/2/open_events?and_text=False&country=ru&offset=0&city=moscow&format=json&limited_events=False&topic=softwaredev&photo-host=public&page=20&radius=25.0&desc=False&status=upcoming&sig_id=217245830&sig=8d781e745933a2834f3bce922830defd7dc12d53"
stringFromUrl = requests.get(url)
pJson = json.loads(stringFromUrl.text)
EndCurrentWeek = time.time() + 604800 
result = ("<html><head></head><body>") 
CurrentWeekday = ""

for (i,temp) in enumerate(pJson["results"]):
    if "venue" in temp: 
        moment = temp["time"]/1000 
        if moment > time.time() and moment < EndCurrentWeek: 
            moment = time.ctime(moment) 
            
            if (CurrentWeekday != moment[0:3]):
                result = result + "<br><h1>" + moment[0:3] + "</h1>"
            CurrentWeekday = moment[0:3]
                
            result  += "<h1>" + moment + "</h1>" 
            result = result + "<h2>" + temp["name"] + "</h2>"
            result = result + "<h3>" + temp["venue"]["city"] + "</h3>"
            result = result + "<h3>" + temp["venue"]["name"] + "</h3>"
            result = result + "<h3>" + temp["venue"]["address_1"] + "</h3>"
            result = result + "<br>" + temp["description"] + "</br>"

result = result + "</body></html>"

f = open('result.html', 'w+') 
f.write(result)
f.close()
print ('check result file in directoru, and use Internet Explorer for watch')
