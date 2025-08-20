from django.urls import path
from . import views

app_name = 'aplicacion'

urlpatterns = [
    path('', views.home, name='home'),
]
