from http import client
from multiprocessing.connection import Client
from django.test import TestCase
from django.urls import reverse
from mywatchlist.views import *

# Create your tests here.

class html_mywatchlist (TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)
        
class xml_mywatchlist (TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)
        
class json_mywatchlist (TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)