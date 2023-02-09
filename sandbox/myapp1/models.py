from django.db import models

class Workers(models.Model):
    name = models.CharField(max_length= 25, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(default=0)
