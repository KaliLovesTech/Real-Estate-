from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Property
from .serializers import PropertySerializer
import requests
from django.http import JsonResponse

# API viewset for properties
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = {
        'city': ['exact'],
        'state': ['exact'],
        'price': ['gte', 'lte'],
        'bedrooms': ['gte', 'lte'],
        'bathrooms': ['gte', 'lte'],
        'square_footage': ['gte', 'lte'],
        'lot_size': ['gte', 'lte'],  # Filtering for lot size
        'year_built': ['gte', 'lte'],  # Filtering for year built
        'property_type': ['exact'],
    }
    search_fields = ['description', 'address']  # Enable search for keywords in description and address
    ordering_fields = ['price', 'square_footage', 'year_built']  # Ordering by year built

# Zillow API search for properties (AJAX calls can use this)
def search_properties(request):
    location = request.GET.get('location', 'Houston, TX')
    status = request.GET.get('status', 'forSale')
    price_type = request.GET.get('priceType', 'listPrice')
    listing_type = request.GET.get('listingType', 'agent')

    url = "https://zillow-com4.p.rapidapi.com/properties/search"
    querystring = {
        "location": location,
        "status": status,
        "priceType": price_type,
        "listingType": listing_type,
    }
    
    headers = {
        "x-rapidapi-key": "847ba95febmshc5c3ba75afc88a2p1ec10bjsnf5eb2eaa4310",  # Replace with your API key
        "x-rapidapi-host": "zillow-com4.p.rapidapi.com"
    }
    
    # Disable SSL verification temporarily
    try:
        response = requests.get(url, headers=headers, params=querystring, verify=False)
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({"error": f"Unable to fetch data: {response.status_code}"}, status=response.status_code)
    except requests.exceptions.SSLError as e:
        return JsonResponse({"error": "SSL Error: {}".format(e)}, status=500)

# HTML template views
def home(request):
    return render(request, 'listings/home.html')

def listings(request):
    properties = Property.objects.all()  # Query all properties from the database
    return render(request, 'listings/listings.html', {'properties': properties})

def property_details(request, id):
    property = Property.objects.get(id=id)
    return render(request, 'listings/property_details.html', {'property': property})
