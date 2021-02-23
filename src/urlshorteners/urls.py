from django.urls import path

from . import views

app_name = 'urlshorteners'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<str:uid>/', views.go_to, name='go_to'),
    path('', views.get_all, name='get_all'),
]
