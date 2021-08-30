from django.urls import path
from .views import homePage, done_attack

urlpatterns = [
    path('', homePage, name="homePage"),
    path('done-attack', done_attack),
]
