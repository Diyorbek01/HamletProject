from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField


# class View(models.Model):
#     name = models.CharField(max_length=20, default=1)



class Region(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=30)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Type(models.Model):
#     name = models.CharField(max_length=10)


class Status(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


        
class Announcment(models.Model):
    title = models.CharField(max_length=25)
    # content = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    # address = models.CharField(max_length=60)
    # type = models.CharField(max_length=10)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    price = models.FloatField()
    features = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'pictures')
    author = models.CharField(max_length=25)

    def __str__(self):
        return self.title

class SubscribedUser(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email