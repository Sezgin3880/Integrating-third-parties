from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Simple home page view."""
    return HttpResponse("<h1>Welcome to Integrating Third Parties Django Project</h1>")
