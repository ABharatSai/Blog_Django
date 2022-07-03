from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('single/<slug:slug>', views.single, name='single'),
    path('aboutus', views.aboutus, name='aboutus'),
]
