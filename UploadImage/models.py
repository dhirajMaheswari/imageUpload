from django.db import models

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=50)
    your_image = models.ImageField(upload_to='images/')
