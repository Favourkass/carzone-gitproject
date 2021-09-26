from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    all_cars = Car.objects.order_by('-created_date')
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'teams': teams, 
        'featured_cars': featured_cars, 
        'all_cars': all_cars,
    }

    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def services(request):
    return render(request, 'pages/services.html')