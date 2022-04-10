from django.shortcuts import render
import folium
def index(request):
    return render(request, "index.html")

