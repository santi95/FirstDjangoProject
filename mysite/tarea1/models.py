from django.db import models


# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        return self.comment
