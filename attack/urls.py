from django.urls import path
from .views import sms_bomber, home_attack, email_attack


urlpatterns = [
    path('attack/', home_attack, name="home_attack"),
    path('sms-bomber/', sms_bomber, name="smsbomber"),
    path('email-attack/', email_attack, name="emailattack"),
]
