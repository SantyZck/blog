from django.db import models
import datetime

class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='Blog/images')
	url = models.CharField(max_length=50)
	date = models.DateField(datetime.date.today)
