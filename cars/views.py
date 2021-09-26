from django.shortcuts import render

# Create your views here.

def cars(request):
    """
    This function renders the cars page.
    """
    return render(request, 'cars/cars.html')