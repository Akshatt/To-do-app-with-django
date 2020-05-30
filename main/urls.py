from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'add_todo/', views.add_todo, name='add_todo'),
]