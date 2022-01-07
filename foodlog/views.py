from django.shortcuts import render
from .models import Food

# Create your views here.

def index(request):
	""" The home page for Foodlog. """
	return render(request, 'foodlog/index.html')

def foods(request):
	"""Show all foods"""
	foods = Food.objects.order_by('date_added')  # imports model
	context = {'foods':foods}  # query database
	return render(request, 'foodlog/foods.html', context)

def food(request, topic_id):
	"""Show a single food and all its entries. """
	food = Food.objects.get(id=topic_id)  # 
	entries = food.entry_set.order_by('-date_added')
	context = {'food':food, 'entries':entries}  # query database
	return render(request, 'foodlog/food.html', context)	