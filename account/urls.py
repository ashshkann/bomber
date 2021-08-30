from django.urls import path
from . views import login_page, register_page, logout_Page
urlpatterns = [
    path('login/', login_page, name='loginPage'),
    path('register/', register_page, name='registerPage'),
    path('logout/', logout_Page, name='logoutPage'),
]
