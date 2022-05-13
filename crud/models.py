from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='POST')

    def __str__(self):
        return self.title