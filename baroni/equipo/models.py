from django.db import models

class Equipo(models.Model):
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  bio = models.TextField()
  position = models.CharField(max_length=100)
  image = models.ImageField(upload_to='equipo_images', null=True, blank=True)  #se debe instalar pillow. upload_to es donde se va a guardar la imangen en la base de datos 

  def __str__(self):
      return self.name
