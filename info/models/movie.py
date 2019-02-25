# Create your models here.
import datetime

from django.db import models
from rest_framework.compat import MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=512)
    year = models.IntegerField(validators=[MinValueValidator(0), ],
                               null=True,
                               blank=True)
    rated = models.CharField(max_length=64,
                             null=True,
                             blank=True)
    released = models.CharField(max_length=64,
                                null=True,
                                blank=True)
    runtime = models.CharField(max_length=64,
                               null=True,
                               blank=True)
    genre = models.CharField(max_length=64,
                             null=True,
                             blank=True)
    director = models.CharField(max_length=512,
                                null=True,
                                blank=True)
    writer = models.CharField(max_length=512,
                              null=True,
                              blank=True)
    actors = models.TextField(null=True,
                              blank=True)
    plot = models.TextField(null=True,
                            blank=True)
    language = models.CharField(max_length=64,
                                null=True,
                                blank=True)
    country = models.CharField(max_length=64,
                               null=True,
                               blank=True)
    awards = models.CharField(max_length=512,
                              null=True,
                              blank=True)
    poster = models.TextField(null=True,
                              blank=True)
    ratings = models.TextField(null=True,
                               blank=True)
    metascore = models.CharField(max_length=64,
                                 null=True,
                                 blank=True)
    imdbrating = models.CharField(max_length=64,
                                  null=True,
                                  blank=True)
    imdbvotes = models.CharField(max_length=64,
                                 null=True,
                                 blank=True)
    imdbid = models.CharField(max_length=64,
                              null=True,
                              blank=True)
    type = models.CharField(max_length=64,
                            null=True,
                            blank=True)
    dvd = models.CharField(max_length=64,
                           null=True,
                           blank=True)
    boxoffice = models.CharField(max_length=512,
                                 null=True,
                                 blank=True)
    production = models.CharField(max_length=512,
                                  null=True,
                                  blank=True)
    website = models.CharField(max_length=512,
                               null=True,
                               blank=True)

    def __str__(self):
        return f'{self.title}'

    def total_comments(self, request):
        from_date = request.query_params.get('from_date', None)
        to_date = request.query_params.get('to_date', None)
        if from_date and to_date:
            from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
            to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
            return self.comments.filter(created__lte=to_date, created__gte=from_date).count()
        else:
            return self.comments.all().count()
