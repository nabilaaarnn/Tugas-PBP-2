from django.db import models

# Create your models here.

class mywatchlist(models.Model):
    watched = models.CharField(max_length=255)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()