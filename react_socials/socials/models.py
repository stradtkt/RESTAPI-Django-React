from django.db import models

class User(models.Model):
	name = models.CharField(max_length=125)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=30)
	age = models.PositiveIntegerField()
	status = models.CharField(max_length=255)
	bio = models.TextField()
