# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	uname = models.CharField(max_length=20)
	pwd = models.CharField(max_length = 20)	

	def __init(self):
		return  self.uname + '-'+ self.pwd


class WorkOut(models.Model):
	wname = models.CharField(max_length=400)
	wtype =  models.CharField(max_length=100)
	body_part = models.CharField(max_length=200)


class UserWorkoutSet(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	workout = models.ForeignKey(WorkOut,on_delete=models.CASCADE)
	set_no = models.IntegerField()	
	weight = models.IntegerField()
	reps = models.IntegerField(default = 1)
	duration = models.IntegerField()
	date = models. DateField()
