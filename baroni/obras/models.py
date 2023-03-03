from django.db import models

class Obra(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    area = models.IntegerField()
    description = models.TextField()    
    credit = models.BooleanField()
    """ imagen = models.CharField(max_length=200)"""
    image = models.ImageField(upload_to='obra_images', null=True, blank=True) #se debe instalar pillow  

    def __str__(self):
        return self.name
