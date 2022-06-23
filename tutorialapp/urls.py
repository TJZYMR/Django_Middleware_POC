from django.urls import path

from tutorialapp.views import hello, exception

urlpatterns = [
    path("hello/", hello),
    path("exception/", exception)#TODO demo extension used in tutorialapp
]