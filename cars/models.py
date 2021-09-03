from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    miliage = models.PositiveIntegerField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='cars_image')
    new = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.year}'
