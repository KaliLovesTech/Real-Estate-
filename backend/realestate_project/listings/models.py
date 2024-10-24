from django.db import models

class Property(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    bedrooms = models.IntegerField(default=1)  # Default 1 bedroom
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)  # Default 1 bathroom
    square_footage = models.IntegerField(default=1000)  # Provide a sensible default value, e.g., 1000 sqft
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, default=0.1)  # Default lot size, e.g., 0.1 acres
    year_built = models.IntegerField(default=2000)  # Default year built, e.g., year 2000
    property_type = models.CharField(max_length=50, choices=[('House', 'House'), ('Condo', 'Condo'), ('Apartment', 'Apartment'), ('Land', 'Land')], default='House')  # Default to 'House'
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address



