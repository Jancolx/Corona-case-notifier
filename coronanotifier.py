import requests
from plyer import notification
from bs4 import BeautifulSoup
from bs4 import Comment

def notifye(title, message): 
    notification.notify(
        
        title=title,
        
        message=message,

        ticker="coronanotifier", app_icon="C://Users//Jancol//Desktop//New folder//coronanotifier. timeout-18



def getData(url):

    r=requests.get(url) 
    
    return r.text



mydata-getData("https://www.mygov.in/covid-19/") 

soup=BeautifulSoup(mydata, 'html.parser")

x=soup.find_all('div'.{"class":"views-row"}) 

for i in x:

    s= i.find('span',{"class":"st_namo"})

    if s.get_text() == "Odisha": 
        y=i.find('div',{"class":"tick-active"}) 
        msgl="Active Cases: "+y.get_text()[7: ]
        z=i.find("div",{"class": "tick-total-vaccine"})
        msg2-"Vaccination: "+z.get_text()[12: ]

title="Odisha"
msg=msg1+"\n"+msg2 
notifyMe(title,msg)   