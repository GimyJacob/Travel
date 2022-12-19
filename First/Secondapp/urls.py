from . import views
from django.urls import path

urlpatterns = [
    path('register/register', views.register, name='register'),
    path('login/login', views.login, name='login'),
    path('logout/',views.logout,name='logout')
]
