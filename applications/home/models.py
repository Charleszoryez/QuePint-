from django.db import models

# Create your models here.
class Persona(models.Model):
    name = models.CharField(max_length = 100, null = False, blank = False, )
    ci = models.IntegerField(primary_key = True,null = False, blank = False)
    email = models.EmailField(null = False,blank = False)
    password = models.TextField(null = False,blank = False)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
    def __str__(self):
        return self.name

class Evento(models.Model):
    nameEvent = models.TextField(max_length = 200,null = False, blank = False)
    organizer = models.CharField(max_length = 100,null = False,blank = False)
    category = models.CharField(max_length = 50,null = False, blank = False)
    description = models.TextField(null = False,blank = False)
    gallery = models.ImageField(max_length = 100,null = False,)
    city = models.CharField(max_length = 100,null = False,blank = False)
    department = models.CharField(max_length = 100,null = False,blank = False)
    country = models.CharField(max_length = 100,null = False,blank = False)
    #gpslength =
    #gpslatitude =
    startDate = models.DateField(null = False,blank = False)
    endingDate = models.DateField(null = False,blank = False)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.nameEvent
