from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import JsonResponse
import requests
import json
# from deep_translator import GoogleTranslator, LingueeTranslator
# from .forms import TForm



# req to endpoint here --->  

# def translate(request):


#     return render(request, "index.html")


def real_time(request):
    if request.method == "POST":
        pasted_text = request.POST["text"]
        payload = {"text":pasted_text}
        url = "API URL HERE....."
        r = requests.post(url,json=payload)
        result = r.json()
        final_result = result["dataToreturn"]
        print(final_result["fake_probability"], final_result["real_probability"])

        depth_value = 0.5
        max_value = ""

        if final_result["real_probability"] > depth_value:
            max_value =  "Humans"
            # print("Human"; max_value)
        else:
            max_value = "Robots"
            # print("Robots"; max_value)
            # print("my name is isaac")
    else:
        return render(request,"index.html")


    context = {"max_value":max_value}
    return render(request,"index.html",context)










      

