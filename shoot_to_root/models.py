from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	#phone=models.CharField(max_length=12)
	comment=models.TextField(max_length=5000)

class User(models.Model):
	name=models.CharField(max_length=50)
	key=models.CharField(max_length=50,default='')
	point=models.IntegerField(default=0)
	
class Comment(models.Model):
	comments=models.TextField(max_length=5000)

class Flag(models.Model):
	index=models.IntegerField(default=0)
	flag=models.TextField(max_length=100)

class Post(models.Model):
	title=models.CharField(max_length=100)
	index=models.IntegerField(default=0)
	description=models.TextField()
	timestamp=models.DateTimeField(default=timezone.now)
	img=models.ImageField(upload_to='')

	def _str_(self):
		return self.title

class CTF(models.Model):
	cate=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	index=models.IntegerField(default=0)
	flag=models.TextField(max_length=100,default='')
	description=models.TextField()
	timestamp=models.DateTimeField(default=timezone.now)
	file=models.FileField(upload_to='',null=True)

	def _str_(self):
		return self.title
