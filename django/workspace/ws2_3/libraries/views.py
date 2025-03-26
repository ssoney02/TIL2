from django.shortcuts import render
import os
import requests
from dotenv import load_dotenv
from pprint import pprint


# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    load_dotenv()

    API_URL = ' http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = os.getenv('ttbkey')
    params = {
        'ttbkey': API_KEY,
        'SearchTarget': 'Book', #(기본값)
        'Output': 'js',
        'QueryType': 'ItemNewSpecial',
        'MaxResults': 50,
        'Version': 20131101     # 얘추가하니까 작동됨 뭥미....
        
    }

    rp = requests.get(API_URL, params=params)

    data = rp.json()

    context = {
        'books': data.get('item')
         }
    return render(request, 'recommend.html', context)
    # 'books'를 템플릿으로 전달