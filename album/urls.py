from django.urls import path, include
from .import views

app_name = 'album'

urlpatterns = [
    path('',views.sadika,name='sadika')
]
