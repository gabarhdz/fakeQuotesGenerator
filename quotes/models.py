from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField(max_length=700,null=False, blank=False)
    

