from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 


# Create your views here.

def cars(request):
    """
    This function renders the cars page.
    """
    cars = Car.objects.order_by('-created_date')
    parginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = parginator.get_page(page)
    data = { 'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):

    """
    This function renders the car details page.
    """
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car' : single_car,
    }
    return render(request, 'cars/car_detail.html', data)