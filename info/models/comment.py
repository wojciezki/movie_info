from django.contrib.postgres.fields import JSONField
from django.db import models
from . import Movie


# Create your models here.


class Comment(models.Model):

    body = models.TextField()

    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name='comments')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.id}-{self.body}'

