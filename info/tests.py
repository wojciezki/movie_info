from rest_framework.test import APITestCase, APIClient

from .models import Movie, Comment


# Create your tests here.


class MovieViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.movies_list_url = '/movies/'
        self.title1 = 'Bronson'
        self.title2 = 'Jungle Book'

    def test_create_movie(self):
        response = self.client.post(self.movies_list_url, {"title": self.title1})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Movie.objects.get(title=self.title1).title, self.title1)
        self.assertEqual(Movie.objects.all().count(), 1)

        response = self.client.post(self.movies_list_url, {"title": self.title2})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Movie.objects.get(title=self.title2).title, self.title2)
        self.assertEqual(Movie.objects.all().count(), 2)

        response = self.client.post(self.movies_list_url, {"title": self.title2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Movie.objects.all().count(), 2)

    def test_movies_list_view(self):
        self.assertEqual(Movie.objects.all().count(), 0)

        self.client.post(self.movies_list_url, {"title": self.title1})
        response = self.client.get(self.movies_list_url)
        self.assertEqual(len(response.data['results']), 1)

        self.client.post(self.movies_list_url, {"title": self.title2})
        response2 = self.client.get(self.movies_list_url)
        self.assertEqual(len(response2.data['results']), 2)


class CommentViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.body1 = "Body1"
        self.body2 = "Body2"
        self.comments_list_url = '/comments/'
        self.movies_list_url = '/movies/'
        self.title1 = "Bronson"
        self.title2 = "Jungle Book"

        self.client.post(self.movies_list_url, {"title": self.title1})
        self.movie1 = Movie.objects.all().first()

        self.client.post(self.movies_list_url, {"title": self.title2})
        self.movie2 = Movie.objects.all().last()

    def test_create_comment(self):
        response = self.client.post(self.comments_list_url, {"body": self.body1,
                                                             "movie": self.movie1.id})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.all().count(), 1)
        self.assertEqual(Movie.objects.get(title=self.title1).comments.all().count(), 1)
        response1 = self.client.post(self.comments_list_url, {"body": self.body1,
                                                              "movie": self.movie1.id})
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(Comment.objects.all().count(), 2)
        self.assertEqual(Movie.objects.get(title=self.title1).comments.all().count(), 2)

    def test_comments_list_view(self):
        self.assertEqual(Comment.objects.all().count(), 0)

        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie1.id})
        response = self.client.get(self.comments_list_url)
        self.assertEqual(len(response.data['results']), 1)

        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie1.id})
        response2 = self.client.get(self.comments_list_url)
        self.assertEqual(len(response2.data['results']), 2)

        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie2.id})
        ### Filter tests
        response3 = self.client.get(self.comments_list_url + f"?movie={self.movie1.id}")
        self.assertEqual(len(response3.data['results']), 2)

        response4 = self.client.get(self.comments_list_url + f"?movie={self.movie2.id}")
        self.assertEqual(len(response4.data['results']), 1)


class TopViewTest(APITestCase):

    def setUp(self):
        client = APIClient()
        self.title1 = "Bronson"
        self.title2 = "Godfather"
        self.title3 = "Hobbit"
        self.title4 = "Avatar"

        self.body1 = "body1"

        self.movies_list_url = '/movies/'
        self.comments_list_url = '/comments/'
        self.top_url = '/top/'

        client.post(self.movies_list_url, {"title": self.title1})
        client.post(self.movies_list_url, {"title": self.title2})
        client.post(self.movies_list_url, {"title": self.title3})
        client.post(self.movies_list_url, {"title": self.title4})

        self.movie1 = Movie.objects.filter()[0]
        self.movie2 = Movie.objects.filter()[1]
        self.movie3 = Movie.objects.filter()[2]
        self.movie4 = Movie.objects.filter()[3]

    def test_top_view(self):

        response = self.client.get(self.top_url)

        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]['rank'], 1)
        self.assertEqual(response.data[1]['rank'], 1)
        self.assertEqual(response.data[2]['rank'], 1)
        self.assertEqual(response.data[3]['rank'], 1)

        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie1.id})
        response = self.client.get(self.top_url)

        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]['rank'], 1)
        self.assertEqual(response.data[1]['rank'], 2)
        self.assertEqual(response.data[2]['rank'], 2)
        self.assertEqual(response.data[3]['rank'], 2)

        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie2.id})
        response = self.client.get(self.top_url)

        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]['rank'], 1)
        self.assertEqual(response.data[1]['rank'], 1)
        self.assertEqual(response.data[2]['rank'], 2)
        self.assertEqual(response.data[3]['rank'], 2)

        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie1.id})
        response = self.client.get(self.top_url)

        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]['rank'], 1)
        self.assertEqual(response.data[1]['rank'], 2)
        self.assertEqual(response.data[2]['rank'], 3)
        self.assertEqual(response.data[3]['rank'], 3)

        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie1.id})
        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie2.id})
        self.client.post(self.comments_list_url, {"body": self.body1,
                                                  "movie": self.movie3.id})
        response = self.client.get(self.top_url)

        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['rank'], 1)
        self.assertEqual(response.data[1]['rank'], 2)
        self.assertEqual(response.data[2]['rank'], 3)




















