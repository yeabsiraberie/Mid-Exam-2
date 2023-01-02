from django.urls import path
from . import views

urlpatterns = [
     
     path('listea/',views.listea),
     path('settea/',views.settea),
     path('deltea/<str:pk>/',views.deltea),
]