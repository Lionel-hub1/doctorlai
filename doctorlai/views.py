"""Views for the doctorlai app."""
from django.shortcuts import render


def index(request):
    return render(request, "index.html")