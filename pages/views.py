from django.shortcuts import render
from listings.models import Listings
from realtors.models import Realtor
# Create your views here.
def index(request):
    listings = Listings.objects.order_by('-list_date')[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors': realtors
    }
    return render(request, 'pages/about.html', context)
