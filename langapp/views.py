from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import JsonResponse
import requests
import json
# from deep_translator import GoogleTranslator, LingueeTranslator
# from .forms import TForm



# req to endpoint here --->  POST https://bb6fnfihh4.execute-api.eu-central-1.amazonaws.com/production/textDetector


def translate(request):


    return render(request, "index.html")


def real_time(request):
    if request.method == "POST":
        pasted_text = request.POST["text"]
        payload = {"text":pasted_text}
        url = "https://bb6fnfihh4.execute-api.eu-central-1.amazonaws.com/production/textDetector"
        r = requests.post(url,json=payload)
        result = r.json()
        final_result = result["dataToreturn"]
        print(final_result["fake_probability"], final_result["real_probability"])

        depth_value = 0.5
        max_value = ""

        if final_result["real_probability"] > depth_value:
            max_value = str(final_result["real_probability"] * 100) +"Humans"
            # print("Human"; max_value)
        else:
            max_value = str(final_result["fake_probability"] * 100) +" Robots"
            # print("Robots"; max_value)
            # print("my name is isaac")

        # print(max_value)  context here....
        return render(request,"index.html",context)




# result = requests.post("https://bb6fnfihh4.execute-api.eu-central-1.amazonaws.com/production/textDetector",text="I LOVE CODING AND SOFTWARE")

# import requests
# import json

# url = "http://192.168.7.2:8000/api/login"










      

