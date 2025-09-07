from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.id =1
    dest1.name ="Bali"
    dest1.desc = "Tropical paradise"
    dest1.price = 500
    dest1.image = "bali.jpg"
    dest2 = Destination()
    dest2.id =2
    dest2.name ="Paris"
    dest2.desc = "City of Lights"
    dest2.price = 800
    dest2.image = "paris.jpg"
    dest3 = Destination()
    dest3.id =3
    dest3.name ="Kashmir"
    dest3.desc = "Heaven on earth"
    dest3.price = 600
    dest3.image = "kashmir.jpg"
    destinations = [ dest1 , dest2 , dest3]
    return render (request , 'index.html' , {'dests':destinations})