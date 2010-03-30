from django.db import models

# Create your models here.



class Tweet(models.Model):
	message = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.message

class Following(models.Model):
	username = models.CharField(max_length = 30)
	
	def __unicode__(self):
		return self.username

class Follower(models.Model):
	username = models.CharField(max_length = 30)
	def __unicode__(self):
		return self.username


class account(models.Model):
	username = models.CharField(max_length = 30)
	tweets = models.ManyToManyField(Tweet)
	following = models.ManyToManyField(Following)
	followers = models.ManyToManyField(Follower)

	def __unicode__(self):
		return self.username
	
