from django.shortcuts import render

# Create your views here.

def index(request):
	""" The home page for Foodlog. """
	return render(request, 'foodlog/index.html')
