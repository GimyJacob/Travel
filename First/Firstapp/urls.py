from . import views
from django.urls import path

urlpatterns = [

    #path('', views.demo, name='demo'),
    path('', views.about, name='about'),
    #  path('contact/',views.contact,name='contact')
]
