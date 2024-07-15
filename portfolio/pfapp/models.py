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


class ProfessionalSkills(models.Model):
    skill1 = models.CharField(max_length=50, blank=True, null=True, default=None)
    skill2 = models.CharField(max_length=50, blank=True, null=True, default=None)
    skill3 = models.CharField(max_length=50, blank=True, null=True, default=None)
    skill4 = models.CharField(max_length=50, blank=True, null=True, default=None)
    skill5 = models.CharField(max_length=50, blank=True, null=True, default=None)
    skill6 = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return self.skill1

    def save(self, *args, **kwargs):
        if not self.pk:
            if ProfessionalSkills.objects.exists():
                raise ValueError("Only one instance of SingleInstanceModel is allowed")
        super().save(*args, **kwargs)


class Languages(models.Model):
    l1 = models.CharField(max_length=50, blank=True, null=True, default=None)
    l2 = models.CharField(max_length=50, blank=True, null=True, default=None)
    l3 = models.CharField(max_length=50, blank=True, null=True, default=None)
    l4 = models.CharField(max_length=50, blank=True, null=True, default=None)
    l5 = models.CharField(max_length=50, blank=True, null=True, default=None)
    l6 = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return self.l1

    def save(self, *args, **kwargs):
        if not self.pk:
            if Languages.objects.exists():
                raise ValueError("Only one instance of SingleInstanceModel is allowed")
        super().save(*args, **kwargs)


class PrivacyPolicy(models.Model):
    header = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.header
