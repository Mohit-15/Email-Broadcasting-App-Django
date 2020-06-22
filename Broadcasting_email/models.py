from django.db import models
#from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class EmailDetail(models.Model):
	email = models.EmailField(_('email'),max_length = 30, unique = True)
	name = models.CharField(_('name'), max_length= 20)

	def __str__(self):
		return self.email

class Message(models.Model):
	message = models.TextField(_('message'), blank=True, null=True)
	name = models.CharField(_('name'), max_length= 20)

	def __str__(self):
		return self.name