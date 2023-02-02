from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class TrafficLight(models.Model):

    text = models.CharField(max_length=50, blank=True, null=True)
    islighton = models.BooleanField(default=False)


    class Meta:
        verbose_name = _('Traffic Light')
        verbose_name_plural = _('Traffic Lights')

    def save(self, *args, **kwargs):
        self.text = "Traffic Light is On." if self.islighton == True  else "Traffic Light is Off."
        return super(TrafficLight, self).save(*args, **kwargs)
        

    def __str__(self)-> str:
        return f"{self.islighton} -> {self.text}"