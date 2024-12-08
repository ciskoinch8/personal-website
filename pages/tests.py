from django.test import SimpleTestCase

class HomepapeTests(SimpleTestCase):
    def test_url_exists_at_location(self):
        reponse = self.client.get("/")
        self.assertEqual(reponse.status_code, 200)

class AboutpapeTests(SimpleTestCase):
    def test_url_exists_at_location(self):
        reponse = self.client.get("/about/")
        self.assertEqual(reponse.status_code, 200)