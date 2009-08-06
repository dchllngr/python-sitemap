
import unittest
import os
from urlparse import urlparse

from sitemap import *

class TestUrlSet(unittest.TestCase): 
     
    def setUp(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.small_sitemap = "%s/fixtures/sitemap.xml" % self.base_path

    def checkContent(self, urlset):
        for url in urlset:
            parts = urlparse(url.loc)
            self.assertEquals(parts.netloc, 'www.example.com')
       
    def testParseFile(self):
        urlset = UrlSet.from_file(self.small_sitemap)
        self.checkContent(urlset)
       
    def testParseString(self):
        content = open(self.small_sitemap).read()
        urlset = UrlSet.from_str(content)
        self.checkContent(urlset)

