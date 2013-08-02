#basic idea: display weather in your area. 
#use openweather API
#interface should be super clean and professional looking.
#controls, simple and keyboard based. 

import json

def getdata(city):
  unit="metric"
  lang="en"
  forecast=3
  datanow=urllib('http://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&lang={2}'.format(city,unit,lang))
  dataforecast=urllib('http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&units={1}&lang={2}&cnt={3}'.format(city,unit,lang,forecast))
  
def splitjsondata(jsondata):
  pass
  
def geticon(weathercode):  
  icon=urllib('http://openweathermap.org/img/w/{0}'.format(weathercode))
  
def savepref():
  #save recent cities
  #save favorites
  

#display window (cairo) with the appropriate information and graphics
