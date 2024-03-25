# lalibela_tourism/tourism/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('attractions/', views.attraction_list, name='attraction_list'),
    path('attractions/<int:attraction_id>/', views.attraction_detail, name='attraction_detail'),
    path('attractions/add/', views.attraction_create, name='attraction_create'),
    path('attractions/<int:attraction_id>/update/', views.attraction_update, name='attraction_update'),
    path('attractions/<int:attraction_id>/delete/', views.attraction_delete, name='attraction_delete'),
    # Add more URL patterns as needed...
]
