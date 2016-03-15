from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
	UserFrom = models.ForeignKey('auth.User', null=True, related_name='sender')
	UserTo	 = models.ForeignKey('auth.User', null=True, related_name='recipient')

	Date = models.DateTimeField(default=timezone.now)

	Text = models.TextField()

	Readed = models.BooleanField(default = False)

	def __str__(self):
		return self.Text
