import pytest
from django.test import LiveServerTestCase
from selenium import webdriver

class TestBrowser(LiveServerTestCase):
    def test_example(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get(("%s%s" % (self.live_server_url, "/admin")))
        assert "Log in | Django site admin" in driver.title