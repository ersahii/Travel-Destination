from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.id = 1
    dest1.name = "Bali"
    dest1.desc = "Tropical paradise"
    dest1.price = 500
    dest1.image = "bali.jpg"

    dest2 = Destination()
    dest2.id = 2
    dest2.name = "Paris"
    dest2.desc = "City of Lights"
    dest2.price = 800
    dest2.image = "paris.jpg"

    dest3 = Destination()
    dest3.id = 3
    dest3.name = "Kashmir"
    dest3.desc = "Heaven on earth"
    dest3.price = 600
    dest3.image = "kashmir.jpg"

    dest4 = Destination()
    dest4.id = 4
    dest4.name = "Dubai"
    dest4.desc = "Luxury in the desert"
    dest4.price = 700
    dest4.image = "paris.jpg"

    dest5 = Destination()
    dest5.id = 5
    dest5.name = "New York"
    dest5.desc = "The city that never sleeps"
    dest5.price = 900
    dest5.image = "bali.jpg"

    dest6 = Destination()
    dest6.id = 6
    dest6.name = "Tokyo"
    dest6.desc = "Land of the Rising Sun"
    dest6.price = 750
    dest6.image = "kashmir.jpg"

    destinations = [dest1, dest2, dest3, dest4, dest5, dest6]
    return render(request, 'index.html', {'dests': destinations})
