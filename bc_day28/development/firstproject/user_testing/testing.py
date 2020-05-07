
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
import time

class FunctionalTesting(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		staging_server = os.environ.get('STAGING_SERVER')
		if staging_server:
			self.live_server_url = 'http://'+staging_server

	def tearDown(self):
		self.browser.quit()

class TestHomePageSuccess(FunctionalTesting):
	def test_signup_login_success(self):
		self.browser.get(self.live_server_url)
		# time.sleep(10)
		h1_tags = self.browser.find_elements_by_tag_name('h1')
		headings = [h1.text for h1 in h1_tags]
		self.assertIn('Post List', headings)

help(TestSignupLoginSuccess)