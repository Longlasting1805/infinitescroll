from django.db import models


# Create your models here.

class UserPostModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(max_length=None, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
