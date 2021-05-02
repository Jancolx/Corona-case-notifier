from plyer import notification
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=15
    )

def getData(url):
    r=requests.get(url)
    return r.text

mydata=getData("https://www.mygov.in/covid-19/")
soup=BeautifulSoup(mydata,'html.parser')
x=soup.find_all('div',{"class":"views-row"})
for i in x :

    state= i.find('span',{"class":"st_name"})
    if state.get_text() == "Odisha":
        active= i.find('div',{"class":"tick-active"})
        msg1 = "Active Cases : "+ active.get_text()[7: ]
        vaccine=i.find('div',{"class":"tick-total-vaccine"})
        msg2="Vaccination: "+ vaccine.get_text()[12: ]

    
title ="Odisha"
msg=msg1+"\n"+msg2
notifyMe(title,msg)