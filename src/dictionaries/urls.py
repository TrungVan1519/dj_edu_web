from django.urls import path

from . import views

app_name = 'dictionaries'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('new/', views.new, name='new'),
    path('<int:id>/delete/', views.delete, name='delete'),
]
