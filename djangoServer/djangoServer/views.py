from django.http import HttpResponse
from .models import collection

def sayHello(request):
    return HttpResponse(collection.count_documents({}))
