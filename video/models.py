from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from datetime import datetime
import os
# Create your models here.

class name_User(models.Model):
	name=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.name.username)

class  userProfile(models.Model):
	uname=models.OneToOneField(User, on_delete=models.CASCADE)
	img=models.FileField()
	dob=models.DateField(null=True,blank=True)
	gender=models.CharField(max_length=30)
	city=models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	def __str__(self):
		return str(self.uname.username)

class Channel(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	name=models.CharField(max_length=255)
	tag_line=models.CharField(max_length=255)
	img=models.FileField(upload_to='upload/img/')
	subscribe=models.IntegerField(default=0)
	pub_date=models.DateTimeField(default=datetime.now())

	def __str__(self):
		return str(self.name)
	

class Videos(models.Model):
	#def __str__(self):
	#	return 'User: ' + self.user.username + ' Name: ' + self.name

    #def was_published_recently(self):
    #	return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))

    #def filename(self):
    #	return os.path.basename(self.video.name)

	user=models.ForeignKey(User, on_delete=models.CASCADE)
	name=models.ForeignKey(Channel, on_delete=models.CASCADE)
	title=models.CharField(max_length=255)
	video=models.FileField(upload_to='upload/')
	img=models.FileField(upload_to='upload/img/')
	category=models.CharField(max_length=255)
	pub_date=models.DateTimeField(default=datetime.now())
	description=models.TextField(max_length=300)
	views=models.IntegerField(default=0)
	like=models.IntegerField(default=0)
	dislike=models.IntegerField(default=0)


class Subscriber(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	sub_name=models.ForeignKey(Channel, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.sub_name)

class Watch(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	viewsid=models.ForeignKey(Videos, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user.username)

class Likes(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	likesid=models.ForeignKey(Videos, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user.username)
		
		