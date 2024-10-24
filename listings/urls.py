from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, search_properties

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('search-properties/', search_properties, name='search_properties'),
]
