# listings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),  # Matches /listings/
    path('property/<int:id>/', views.property_details, name='property_details'),
    path('properties/', views.PropertyViewSet.as_view({'get': 'list'}), name='properties_list'),  # Matches /listings/properties/
]
