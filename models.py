from django.db import models

# Create your models here.

class contactform(models.Model):
	fName=models.CharField(max_length=100)
	lName=models.CharField(max_length=100)
	email=models.EmailField()
	sub=models.TextField()
	msg=models.TextField()
