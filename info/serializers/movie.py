from django.db.models import Count, Prefetch
from rest_framework import serializers

from ..models import Movie, Comment


class MovieBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class TopMovieSerializer(serializers.Serializer):

    rank = serializers.SerializerMethodField()

    total_comments = serializers.SerializerMethodField()

    movie_id = serializers.SerializerMethodField()

    def get_rank(self, obj):
        movies = Movie.objects.all()
        ranks = [movie.total_comments(self.context['request']) for movie in movies]
        ranks = list(set(ranks))
        ranks.sort(reverse=True)
        rank = ranks.index(obj.total_comments(self.context['request'])) + 1
        return rank

    def get_movie_id(self, obj):
        return obj.id

    def get_total_comments(self, obj):
        return obj.total_comments(self.context['request'])