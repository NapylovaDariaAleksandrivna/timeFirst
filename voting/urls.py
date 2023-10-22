
from django.urls import path
from . import views
urlpatterns = [
    
    
    path('last/', views.last, name='last'),
    

]