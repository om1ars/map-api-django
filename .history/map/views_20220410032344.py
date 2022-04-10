from django.shortcuts import render
import folium
def index(request):
    m = folium.Map()
    m = m._repr_html_()
    context = 
    return render(request, "index.html")

