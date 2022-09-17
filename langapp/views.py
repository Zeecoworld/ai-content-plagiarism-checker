from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import JsonResponse
import requests
from deep_translator import GoogleTranslator, LingueeTranslator
# from .forms import TForm



# translated = LingueeTranslator(source='en', target='de').translate("coding is sweet!!!")  # output -> Weiter so, du bist großartig


def translate(request):


    return render(request, "index.html")


def real_time(request):
    try:
        result = ''
        if request.method == "POST":
            Text = request.POST['Text']   #FIX THIS!!!!!!!
            Lang2 = request.POST['Lang2']
            # print(Text,Lang1,Lang2)
            result = GoogleTranslator(source="auto", target=Lang2).translate(Text) 
            # print(result)	
	
        # context = {"result":result}

    except requests.exceptions.RequestException as error:
        result = "Please Try Again..."

        # context = {"result": result}


    return JsonResponse({"result": result})


      

