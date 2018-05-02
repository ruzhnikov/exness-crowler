
# -*- coding: utf-8 -*-


class CrawlerResponse():
    def __init__(self, error=None, warning=None):
        self.__error = error
        self.__warning = warning

    @property
    def success(self):
        if self.has_error:
            return False

        return True
    
    @property
    def has_error(self):
        return False if self.__error is None else True
    
    @property
    def error(self):
        return self.__error
    
    @property
    def has_warning(self):
        return False if self.__warning is None else True
    
    @property
    def warning(self):
        return self.__warning
