from django.shortcuts import render
import json
from django.http import JsonResponse
from . import analysis
from .models import loggy
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def webhook_dbChanges(request):
    if request.method=='POST':
        bytepayload=request.body.decode().replace("'",'"')
        
    payload = json.loads(bytepayload)
    if payload.get("changeType")=="insert_changes":
        tableData=analysis.getTableData(payload.get("model"))
        analysis.analyze(tableData)
        loggy.info("webhook's bussin")
        return JsonResponse({"HeadsUp":"Working on it..."},status=200)
    else:
        return JsonResponse({"HeadsUp":"Invalid"},status=405)