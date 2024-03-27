from django.db import models


# Create your models here.

class houseListingModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.ImageField()
    square_feet = models.IntegerField()
    no_of_bedrooms = models.IntegerField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to= 'uploads/')

    # def __str__(self):
    #     return self.title
