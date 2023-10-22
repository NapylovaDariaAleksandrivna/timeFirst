
from django.urls import path
from . import views

urlpatterns = [
    
    
    path('last/', views.last, name='last'),
    path('', views.home, name='home')

]