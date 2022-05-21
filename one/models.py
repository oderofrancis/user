import email
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	e_mail = models.EmailField()
	phone_number = PhoneNumberField()
	profile_pic = models.ImageField(null=True,blank=True)

	def __str__(self):
		return self.first_name