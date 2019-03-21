from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {}
    return render(request, 'arcgistest/home.html', context)


@login_required()
def interdensity(request):

    context = {}
    return render(request, 'arcgistest/interdensity.html', context)
