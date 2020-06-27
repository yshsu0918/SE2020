from django.shortcuts import render
import requests
import json
# Create your views here.
from django.http import HttpResponse
import time
def hello_world(request):
    url = 'http://140.113.167.23/se2020/product/all'
    r = requests.get(url)
    #print(r.text)
    Q = r.text[1:-1].replace('},{', '}@@@{')
    
    items = []
    for x in Q.split('@@@'):
        #print(x)
        json_object = json.loads(x)
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
        items.append(json_object)
    
    

    current_time = str(time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime()))

    return render(request, 'hello_world.html', locals() )