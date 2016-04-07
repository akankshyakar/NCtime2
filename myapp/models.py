from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MyProfile(models.Model):
	user= models.OneToOneField("auth.User")
	date_of_birth=models.DateField()
 	bio= models.TextField()
