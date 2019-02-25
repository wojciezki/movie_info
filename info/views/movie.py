import json

import requests
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from url_filter.integrations.drf import DjangoFilterBackend

from ..models import Movie
from ..serializers import MovieBaseSerializer, TopMovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    serializers = {
        'default': MovieBaseSerializer,
    }
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('title', 'year', 'actors', 'country')
    ordering_fields = ('title', 'year', 'country')

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def create(self, request, *args, **kwargs):
        movie = Movie.objects.filter(title=request.data['title'])
        if movie:
            serializer = self.get_serializer(movie, many=True)
            return Response(serializer.data, status=200)
        return super(MovieViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer = self._get_movie_info(serializer)
        return super(MovieViewSet, self).perform_create(serializer)

    def _get_movie_info(self, serializer):
        """Get movie info from external api based on movie title
        :param serializer:
        :return: serializer
        """
        title = serializer.validated_data['title']
        movie_info_request = requests.get(f'http://www.omdbapi.com/?apikey=ba315c86&t={title}')
        movie_info_dict = json.loads(movie_info_request.content.decode("utf-8"))
        response = movie_info_dict.pop('Response')
        if response != 'True':
            raise ValidationError("This movie does not exists")
        serializer = self._fill_validated_data_with_data(serializer, movie_info_dict)
        return serializer

    def _fill_validated_data_with_data(self, serializer, movie_info):
        """Fills validated_data with movie info based on response from external api
        :param serializer:
        :param movie_info:
        :return: serializer
        """
        for key, value in movie_info.items():
            serializer.validated_data[key.lower()] = value
        return serializer


@api_view(['GET', ])
def top(request):
    """
    Return movies from top 3 ranks based on comments amount in some time period
    :param request:
    :return:
    """
    movies = Movie.objects.all()
    serializer = TopMovieSerializer(movies, many=True, context={'request': request})
    filtered_list = [movie for movie in serializer.data if movie['rank'] in [1, 2, 3]]
    return Response(filtered_list)
