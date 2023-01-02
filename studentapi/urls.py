from django.urls import path
from . import views

urlpatterns = [
     
     path('lisstu/',views.lisstu),
     path('setstu',views.setstu),
     path('delstu/<str:pk>/',views.delstu),
]