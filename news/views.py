from django.shortcuts import render
import requests
import xmltodict
import json

# Create your views here.

def home(request):  
    raw_data = requests.get(f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey=WU5bDs9ZiQcY%2BRTTeO0fqcZJPZe2Zvhx%2FzztE3nqlpmKKDzv4H84z%2BFh3j3KEKLTC2bKXQa94D0jC5ZPNsuSqQ%3D%3D&numOfRows=10&pageNo=1&sidoName=%EA%B0%95%EC%9B%90&searchCondition=DAILY').content

    xmlObject = xmltodict.parse(raw_data)
    jsonObject = json.loads(json.dumps(xmlObject))

    dataShown = jsonObject['response']['body']['items']['item']
   
    return render(request, 'home.html', {'dataShown':dataShown})

