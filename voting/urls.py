
from django.urls import path
from . import views

urlpatterns = [
    path('last/', views.last, name='last'),
    path('', views.home, name='home'),
    path('voiting/', views.voiting, name='voiting'),
    path('qwertyuiop/', views.for_admin, name='none')
]