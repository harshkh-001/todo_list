from django.contrib import admin
from django.urls import path
from todolist import views
from .views import adding

urlpatterns = [
    path('', views.home, name='home'),
    path('adding' , views.adding , name = "adding"),
    path('return_list' , views.return_list , name = "return_list"),
    path('display' , views.returning , name = "returning"),
    path('signup' , views.sign , name = "signup"),
    path('sign_up' , views.sign_up , name = "sign_up")
    # path('/redirect/' , adding)
]