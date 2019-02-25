from django.db import models
from django.urls import reverse



class SeniorManager(models.Model):
    name=models.CharField(max_length=25)
    designation = models.CharField(max_length=25)
    reporting=models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=25)
    designation=models.CharField(max_length=25)
    reporting=models.ForeignKey(SeniorManager,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=25)
    designation=models.CharField(max_length=25)
    reporting =models.ForeignKey(Manager,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('app85:index')
