from django.contrib import admin
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adding' , views.adding , name = "adding"),
    path('return_list' , views.return_list , name = "return_list"),
    path('display' , views.returning , name = "returning")
]