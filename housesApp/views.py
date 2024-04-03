from django.shortcuts import render
from .models import houseListing  # Assuming your model is named houseListingModel


# Create your views here.(CRUD -CREATE

def house_listing(request):
    """Fetches all listings from the database and renders the 'listings.html' template."""

    listings = houseListing.objects.all()  # Assuming houseListingModel is your model
    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context)
