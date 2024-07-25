import requests
import json

from datetime import datetime,timedelta
today=datetime.now().date()
two_day_back=today-timedelta(days=5)
# robotics url
url_robotics='https://newsdata.io/api/1/news?apikey=pub_34916e75d7f9b537989a78622b752f77f645b&q=robotics&language=en&category=education,science,technology'
url_wie_news='https://newsdata.io/api/1/news?apikey=pub_34916e75d7f9b537989a78622b752f77f645b&q="women%20in%20STEM"&category=technology'
url_ai_machine_learning='https://newsdata.io/api/1/news?apikey=pub_34916e75d7f9b537989a78622b752f77f645b&q="artificial%20neural%20network"%20OR%20"deep%20learning"&language=en&category=technology,top '
response=requests.get(url_ai_machine_learning)
json_data=response.json()

robotics_news=[]
print(json_data)
for result in json_data["results"]:
    robotics_news.append(result)
    
for i in robotics_news:
    print(f"Title: {i.get('title','N/A')}")
    print(f"Link: {i['link']}")



