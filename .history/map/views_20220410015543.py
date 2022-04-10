from django.shortcuts import render
import folium
def index(request):
    m = folium
    return render(request, "index.html")

