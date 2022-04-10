from django.shortcuts import render
import folium
def index(request):
    m = folium.Map()
    m._repr_html
    return render(request, "index.html")

