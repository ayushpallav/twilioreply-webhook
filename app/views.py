import json
import requests
import urllib.parse
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
# from .models import webhookTransaction
# from .serializers import get_resp

# def check_for_msg(request):


@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    jsonData = request.body
    url_params = jsonData.decode('utf-8')
    params_dict = urllib.parse.parse_qs(url_params)
    params = dict(params_dict)
    print(params)
    jData = json.dumps(params)
    y = json.loads(jData)

    def conv(o):
        if(isinstance(o,datetime)):
            return o.__str__()
    payload = {             
        "sender":y['From'][0],             
        "body":y['Body'][0],
        # "timestamp":'test'
        "timestamp" : json.dumps(datetime.now(), default=conv)          
    }
    # Trigger the workflow / post to another URI 
    # r =  requests.post('https://prod-22.centralindia.logic.azure.com:443/workflows/355add03614e4927afb327f9b7da4d01/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=Tm-Ijn2NVR4O6tWa5j33uGbynuuY9VIB0nT2rEpArKo', json=jData)
    print(r.status_code)
    return HttpResponse('HTTP_200_OK')
