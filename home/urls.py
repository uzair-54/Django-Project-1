from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('development', views.development, name='development'),
    path('courses', views.courses, name='courses'),
    path('game', views.game, name='game'),
    path('web', views.web, name='web'),
    path('ml', views.web, name='ml'),
]
