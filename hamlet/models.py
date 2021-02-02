from django.db import models

class Announcment(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    price = models.FloatField()
    feautures = models.TextField()
    image = models.ImageField(upload_to = 'pictures')
    

    def __str__(self):
        return self.title