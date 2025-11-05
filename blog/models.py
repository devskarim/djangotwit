from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	desc = models.TextField()
	image = models.FileField(upload_to='images/', null=True , blank=True)
	is_published = models.BooleanField(default=True) 
	created_at = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.title