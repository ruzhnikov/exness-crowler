
# -*- coding: utf-8 -*-


import unittest
from resources_crawler.response import CrawlerResponse

class TestCrawlerResponse(unittest.TestCase):
    def test_empty_construct(self):
        response = CrawlerResponse()
        self.assertTrue(response.success)
        self.assertFalse(response.has_error)
        self.assertFalse(response.has_warning)

    def test_with_warn(self):
        warning_str = "This is warning"
        response = CrawlerResponse(warning=warning_str)

        self.assertTrue(response.success)
        self.assertFalse(response.error)
        self.assertTrue(response.has_warning)
        self.assertEqual(response.warning, warning_str)

    def test_with_error(self):
        error_str = "This is error"
        response = CrawlerResponse(error=error_str)

        self.assertFalse(response.success)
        self.assertTrue(response.has_error)
        self.assertEqual(response.error, error_str)
    
    def test_with_everyone(self):
        error_str = "This is error"
        warning_str = "This is warning"

        response = CrawlerResponse(error=error_str, warning=warning_str)

        self.assertFalse(response.success)
        self.assertTrue(response.has_error)
        self.assertTrue(response.has_warning)
        self.assertEqual(response.error, error_str)
        self.assertEqual(response.warning, warning_str)

if __name__ == '__main__':
    unittest.main()
