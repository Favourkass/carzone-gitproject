from django.db import models

# Create your models here.

class Team(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    description = models.TextField()
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    google_plus_link = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname