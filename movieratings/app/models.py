from django.db import models

class Reviewer(models.Model):
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)
    postal_code = models.IntegerField()

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    imdb_link = models.URLField(max_length=255, unique=True)
    director = models.CharField(max_length=99)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=99)

    def __str__(self):
        return self.title

class MovieReview(models.Model):
    reviewer = models.ForeignKey(Reviewer, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
    stars = models.CharField(max_length=12)
    notes = models.TextField()

    def __str__(self):
        return self.movie
