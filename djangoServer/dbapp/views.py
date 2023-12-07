from django.shortcuts import render
from django.http import JsonResponse
from djangoServer.settings import loggy
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def webhook_dbChanges(request):
    if request.method=='POST':
        bytepayload=request.body.decode().replace("'",'"')
        
    payload = json.loads(bytepayload)
    if payload.get("changeType")=="insert_changes":
        #TODO:implement analysis module and then call it here
        loggy.info("yo webhook got hit this shit gonna be bussin!")
        return JsonResponse({"HeadsUp":"Under Construction"})
    else:
        return JsonResponse({"HeadUp":"Invalid request"},status=405)
    
