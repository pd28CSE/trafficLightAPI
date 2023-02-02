from django.db import models

# Create your models here.

class User(models.Model):

    text = models.CharField(max_length=50, blank=True, null=True)
    islighton = models.BooleanField(default=False)


    def __str__(self):
        return str(self.islighton)