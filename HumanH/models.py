from django.db import models


# Create your models here.

class Tutorial(models.Model):
	"""docstring for HumanStory"""

	title = models.CharField(max_length = 200)
	content = models.TextField()
	tutorial_published = models.DateTimeField("date published")
	def __str__(self):
		return self.title 

