# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

FORECASTS = {
    "today" : "https://weather.com/weather/today/l/USIN0211:1:US",
    "five_day" : "http://weather.com/weather/5day/l/USIN0211:1:US"
    }

def MakeRequest(cast):

    # Get the response, parse the HTML, and return
    page = requests.get(FORECASTS.get(cast))
    soup = BeautifulSoup(page.content, 'html.parser')
    
    return soup

def GetFiveDay():

    dayList = []
    dayDict = {
        'Date' : 0,
        'Temp Range' : 0,
        'Desc' : "",
        'Humidity' : 0
        }

    # Get the response
    response = MakeRequest("five_day")

    # Narrow the focus
    fiveDayForecast = response.find(class_="twc-table")
    forecastItems = fiveDayForecast.find_all(class_="clickable closed")   
        
    # Define what we're interested in
    for day in forecastItems:
       dayDict['Date'] = day.find(class_="day-detail clearfix").get_text()
       dayDict['Temp Range'] = day.find(class_="temp").get_text()
       dayDict['Desc'] = day.find(class_="description").get_text()
       dayDict['Humidity'] = day.find(class_="humidity").get_text()
       dayList.append(dayDict)

    print(dayList)

def GetToday():

    dayDict = {
        'Temp Range' : 0,
        'Desc' : "",
        'Now Temp' : 0,
        'Feels' : 0
        }

    # Get the response
    response = MakeRequest("today")

    # Narrow the focus
    todayForecast = response.find(class_="today_nowcard")
            
    # Define what we're interested in
    dayDict['Now Temp'] = todayForecast.find(class_="today_nowcard-temp").get_text()
    dayDict['Temp Range'] = todayForecast.find(class_="today_nowcard-hilo").get_text()
    dayDict['Desc'] = todayForecast.find(class_="today_nowcard-phrase").get_text()
    dayDict['Feels'] = todayForecast.find(class_="today_nowcard-feels").get_text()
    

    print(dayDict)

GetToday()
