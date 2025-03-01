from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete')
]
