from django.db import models

# Create your models here.  A model is a class.

class Food(models.Model):
	"""A food the user is eating."""
	food_name = models.CharField(max_length=20)
	calcium_in_mg  = models.FloatField(max_length=6)
	carbohydrate_in_grams = models.FloatField(max_length=6)
	cholesterol_in_mg = models.FloatField(max_length=6)
	Energy_in_kcal = models.FloatField(max_length=6)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.food_name

class Person(models.Model):
	"""Profile of a user"""
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	height_in_feet  = models.FloatField(max_length=2)
	height_in_inches = models.FloatField(max_length=2)
	age = models.FloatField(max_length=3)
	daily_calorie_limit = models.FloatField(max_length=4)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.first_name