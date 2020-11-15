from django.db import models

# Create your models here.
class Movie(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title_english = models.CharField(max_length=200)
    title_long = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.FloatField()
    runtime = models.IntegerField()
    genres = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.title)