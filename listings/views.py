from ast import keyword
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listings
# Create your views here.
def index(request):
    listings = Listings.objects.order_by('-list_date')
    paginator = Paginator(listings, 6) # Show 6 listings per page.

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)
    context = {
        "listing": listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listings.objects.order_by('-list_date')

    # search by keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Search by City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Search by state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Search by bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    # Search by price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)