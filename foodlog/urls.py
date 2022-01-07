""" Defines URL pattersn for foodlog.  """

# import the path function which is needed when mapping URLS to views
from django.urls import path   

# import views module
# the dot tells Python to import the view.py module from the same
# director as current urls.py module
from . import views

# the variable app_name helps Django distinguish this urls.py file
# from files of the same name in other apps within the project.
app_name = "foodlog"

#  the variable urlpatterns in this module is a list of indiviual
# pages that can be requested from the foodlong app.
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),
	# Page that shows all foods.
	path('foods/', views.foods, name='foods'),
	# Detail page for a single food.
	path('foods/<int:food_ids>/', views.food, name='food')
]