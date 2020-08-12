from django.db import models

# Create your models here

#Employee Model Class
class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(blank=False, unique=True)
    department = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.name)
