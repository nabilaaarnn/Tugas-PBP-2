from django.db import models
from django.contrib.auth.models import User

class todolistItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    done = models.BooleanField(default=False)