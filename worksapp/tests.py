from rest_framework.test import APITestCase
from .models import MusicWorks

class TestMusic(APITestCase):
    url = '/music/ABC1234/'

    def setUp(self):
        MusicWorks.objects.create(title='Good things', contributors='nicki minaj | Dj Khaled | jay-z | P Diddy', iswc='ABC1234')

    def test_iswc_search(self):
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['iswc'], 'ABC1234')
