from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=300)
    about = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="media/")


    