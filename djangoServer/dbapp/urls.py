from django.urls import path
from . import views

urlpatterns = [
    path('dbchanges-webhook',views.webhook_dbChanges)
]
