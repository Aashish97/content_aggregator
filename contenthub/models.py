from django.db import models

# Create your models here.
class Content(models.Model):
    headline = models.CharField(max_length=250, unique=True)
    body = models.CharField(max_length=250)
    image = models.URLField(max_length = 250) 
    link = models.URLField(max_length = 250) 
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.headline + "(" + self.tag + ")"