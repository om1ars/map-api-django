from django.shortcuts import render
from folium
def index(request):
    return render(request, "index.html")

