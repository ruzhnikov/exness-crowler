
# -*- coding: utf-8 -*-


class Crawler():
    def __init__(self, loader_object):
        self._obj = loader_object
    
    def process(self, url):
        process_result = self._obj.process(url)
        if type(process_result).__name__ != "CrawlerResponse":
            raise Exception(
                "The reposponse of process must be an object of CrawlerResponse")
        
        return process_result
