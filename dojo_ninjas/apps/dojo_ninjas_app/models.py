from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

    def __unicode__(self):
        return "id : " + str(self.id) + ", name : " + self.name + ", city : " + self.city + ", state : " + self.state

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    laste_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo,on_delete=models.CASCADE, related_name="ninjas")

    def __unicode__(self):
        return "id : " + str(self.id) + ", first_name : " + self.first_name + ", last_name : " + self.last_name + ", dojo : " + str(self.dojo.name)