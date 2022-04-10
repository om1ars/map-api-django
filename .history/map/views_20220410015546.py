from django.shortcuts import render
import folium
def index(request):
    m = folium.MAP
    return render(request, "index.html")

