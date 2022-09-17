from django.urls import path
from . import views


urlpatterns = [

    path('', views.translate, name='home'),
    path('lang/', views.real_time , name='lang'),
  
]