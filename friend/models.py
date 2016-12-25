from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Friend(models.Model):
	user_to = models.ForeignKey(User, related_name='user_to')
	friend_to = models.ForeignKey(User, related_name='friend_to')
	status = models.IntegerField(blank=False, null=False)
	date = models.DateTimeField(auto_now=True, blank=True, null=True)

	def __str__(self):
		WAIT = 1
		ACCETED = 2
		REJECT = 3
		
		user_to = self.user_to
		friend_to = self.friend_to
		status = self.status
		
		if status == WAIT:
			return "%s and %s, en espera" % (user_to, friend_to)

		if status == ACCETED:
			return "%s and %s, aceptado" % (user_to, friend_to)

		if status == REJECT:
			return "%s and %s, rechazado" % (user_to, friend_to)
			
