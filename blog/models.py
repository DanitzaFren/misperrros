from django.db import models
from django.utils import timezone


# Create your models here.


class adop(models.Model):
    correo = models.TextField()
    run = models.CharField(max_length=200)
    nombre = models.TextField()
    fechanac =  models.DateField(
            blank=True, null=True)
    telefono =models.CharField(max_length=200)
    region = models.TextField()
    ciudad =models.TextField()
    tipo = models.TextField()
    fechasol=models.DateField(default=timezone.now())

    def publish(self):
        self.fechasol = timezone.now()
        self.save()

    def __str__(self):
        return self.run
