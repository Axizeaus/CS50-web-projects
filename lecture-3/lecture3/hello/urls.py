from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('greetings', views.greetings, name='greetings'),
    path('<str:name>', views.greet_user, name='greet_user')
]
