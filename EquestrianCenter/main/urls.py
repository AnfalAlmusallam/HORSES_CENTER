from django.urls import path
from .import views

app_name="main"

urlpatterns =[
    path('home/',views.home_page, name='home_page'),
    path('contact/',views.contact,name='contact'),
]