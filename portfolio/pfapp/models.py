from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='static/pfapp/assets/', blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date_range = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.position


class Education(models.Model):
    institution_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    field = models.CharField(max_length=30)
    date_range = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.institution_name
