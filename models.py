from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	img_field = models.ImageField(upload_to='uploads/')
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title