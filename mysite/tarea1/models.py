from django.db import models
import datetime

# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=100)
    date = models.DateField(blank = True, null = True)

    def __str__(self):
        return self.comment
