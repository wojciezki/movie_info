from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from . import views

app_name = 'info'

router = DefaultRouter()

router.register(r'movies', views.MovieViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    url(r'^top/$', views.top, name='top')
]

urlpatterns += router.urls
