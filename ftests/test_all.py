
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase


class HomeNewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        fullUrl = self.live_server_url + reverse(namespace)
        print(fullUrl)
        return fullUrl

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"),
                         "rgba(200, 50, 255, 1)")


# from selenium import webdriver as wd
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.core.urlresolvers import reverse
# class NewHomeVisitorTest(SLST):
#     def setUp(self):
#         self.browser = wd.Firefox()
#         # self.browser.implicitly_wait(1)
#         activate('en')
#     def tearDown(self):
#         self.browser.quit()
#
#     def get_full_url(self, namespace):
#         print("Live server:", str(self.live_server_url))
#         print("Namespace:", str(reverse(namespace)))
#         return self.live_server_url + reverse(namespace)
#
#     def test_home_title(self):
#         print("Testing the home title...")
#         url = self.get_full_url("home")
#         self.browser.get(url)
#         self.browser.implicitly_wait(1)
#         self.assertIn("TaskBuster", self.browser.title)
