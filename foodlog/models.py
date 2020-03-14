from django.db import models

# Create your models here.

class Food(models.Model):
    """A food eaten by user """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Comment(models.Model):
	"""A comment about a specific food """
	food = models.ForeignKey(Food, on_delete=models.CASCADE)
	text = models.CharField(max_length=400)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text  



#class Nutrient(models.Model):
# 	food = models.ForeignKey(Food, on_delete=models.CASCADE)
# 	protein = 'protein'
# 	fat = 'fat'
# 	carbohydrate = 'carbohydrate'

# 	def __str__(self):
# 		"""Return a string representation of the model."""
#      	return self.text