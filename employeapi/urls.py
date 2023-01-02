from django.urls import path
from . import views

urlpatterns = [
     
     path('lisemp/',views.lisemp),
     path('setemp/',views.setemp),
     path('delemp/<str:pk>/',views.delemp),
]