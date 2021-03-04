from django.db import models
from django.urls import reverse
# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length = 40)
    experience = models.FloatField()
    country = models.CharField(max_length = 30)

    def __repr__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length = 50)
    level = models.IntegerField()
    developer = models.ForeignKey(Developer, on_delete =  models.CASCADE)

    def __repr__(self):
        return self.name + " " + self.level
    def get_absolute_url(self):
        return reverse('ninjas:details',args=(self.developer,))