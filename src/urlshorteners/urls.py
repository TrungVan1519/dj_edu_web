from django.urls import path

from . import views

app_name = 'urlshorteners'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<str:uid>/', views.go, name='go'),
    path('', views.index, name='index'),
]
