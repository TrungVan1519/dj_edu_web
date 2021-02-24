from django.urls import path

from . import views

app_name = 'urlshorteners'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<str:uid>/go/', views.go, name='go'),
    path('<int:id>/delete/', views.delete, name='delete'),
]
