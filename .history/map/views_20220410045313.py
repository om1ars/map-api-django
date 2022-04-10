from django.shortcuts import render
import folium
from .models import Search
import geocoder
from .forms import SearchForm


def index(request):
    if request.method == "POST":
        form = SearchForm
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([lat, lng], tooltip="Click for more",
                  popup=country).add_to(m)
    m = m._repr_html_()
    context = {
        "m": m
    }
    return render(request, "index.html",  context)
