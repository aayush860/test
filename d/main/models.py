from django.db import models

# Create your models here.
class tutorials(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_date = models.DateTimeField("date published")
	
	def __str__(self):
		return self.tutorial_title