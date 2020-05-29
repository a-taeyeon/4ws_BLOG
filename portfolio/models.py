from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length = 235)
    image = models.ImageField(upload_to='images/')  #pip install pillow 해줘야함
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title