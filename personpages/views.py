from django.shortcuts import render

from .models import Doughnut

def indexPageView(request):
    # Fetch all doughnuts from the database
    doughnuts = Doughnut.objects.all()

    # Dynamic context for the index page
    context = {
        "page_title": "Home",
        "welcome_message": "Welcome to the Doughnut Shop! Explore our delicious options below.",
        "data": doughnuts,  # Replacing hardcoded data with dynamic data
    }

    return render(request, 'personpages/index.html', context)