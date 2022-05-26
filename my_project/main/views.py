from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from googletrans import Translator
# Create your views here.
def homepage(request):
    city='Osh'
    country='Kyrgyzstan'
    cities = ['osh', 'Bishkek', 'chui', 'batken', 'jalal-abad', 'talas', 'naryn']
    number = [4, 45, -7, 11, -58, 47]
    return render(request, 'index.html', context={'my_city':city,'my_country':country,'my_cities':cities, 'numbers':number})

API_KEY = 'b6fad32d53b445047b0498e182aebaef'
WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'


def weather(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        API_KEY = 'b6fad32d53b445047b0498e182aebaef'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
        response= requests.get(url)
        data = response.json()
        print(data)
        translator = Translator()

        w_cond = translator.translate(data['weather'][0]['description'], dest='ru').text
        icon_id = data['weather'][0]['icon']
        print(icon_id)
        
        weather = f"погода в городе {city_name.title()}: {w_cond}"

        temp = f"Темперура в городе {city_name.title()}:{data['main']['temp']}℃"

        cond = translator.translate(data['weather'][0]['main'], dest='ru').text
        coudd = f"Прагноз пагоды в городе {city_name.title()}:{cond}"

        feels_like = f"Температура в городе {city_name.title()} ощущается как:{data['main']['feels_like']}℃"
        min_temp = f"Минималная температура в городе {city_name.title()} : {data['main']['temp_min']}℃"

        max_temp = f"Максималная температура в городе {city_name.title()} : {data['main']['temp_max']}℃"


        return render(request, 'index.html', {'weather':weather,'temp':temp, 'coudd':coudd, 'feels_like':feels_like, 'min_temp':min_temp, 'max_temp':max_temp, 'icon_id':icon_id} )

