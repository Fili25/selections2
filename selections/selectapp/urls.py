from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html/', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('final.html/', views.final, name='final'),
    path('lk.html/', views.lk, name='lk'),
    path('test.html/', views.test, name='test'),
    path('login.html/', views.login, name='login'),
    
]