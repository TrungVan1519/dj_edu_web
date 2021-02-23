from django.urls import path

from . import views

app_name = 'notebooks'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('', views.index, name='index'),
]
