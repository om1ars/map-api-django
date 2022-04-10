from django.shortcuts import render
import folium
def index(request):
    m = folium.Map()
    
    return render(request, "index.html")

