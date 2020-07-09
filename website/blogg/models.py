from django.utils import timezone
from django.db import models

class Post(models.Model):
	author=models.ForeignKey('auth.user', on_delete=models.PROTECT)
	title=models.CharField(max_length=30)
	text=models.TextField()                      
	created_date=models.DateTimeField(default=timezone.now()) 
	published_date=models.DateField(blank=True,null=True) 
	
	def __str__(self):
		return self.title
