from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    age = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=250, null=True)
    experience = models.CharField(max_length=50, null=True)
    handicap = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    course_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    description = models.CharField(max_length=750, null=True)
    notes = models.CharField(max_length=750, null=True)
    thumbnail = models.CharField(max_length=700, null=True)
    url = models.CharField(max_length=250, null=True)
    price = models.CharField(max_length=250, null=True)
    users = models.ManyToManyField(User, related_name='users', through='Foursome')

    def __str__(self):
        return self.course_name

class Foursome(models.Model):
    day = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    time = models.CharField(max_length=500, null=True)
    course = models.ForeignKey(Course, blank=True, null=True, related_name='foursomes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, related_name='foursomes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'
