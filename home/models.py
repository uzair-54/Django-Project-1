from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name