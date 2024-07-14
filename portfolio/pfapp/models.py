from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='static/pfapp/assets/', blank=True)

    def __str__(self):
        return self.name
