
# -*- coding: utf-8 -*-


class CrawlerResponse():
    def __init__(self, fatal_error=None, non_fatal_error=None):
        self.__fatal_error = fatal_error
        self.__non_fatal_error = non_fatal_error

    @property
    def success(self):
        if self.has_fatal_error:
            return False

        return True
    
    @property
    def has_fatal_error(self):
        return False if self.__fatal_error is None else True
    
    @property
    def fatal_error(self):
        return self.__fatal_error
    
    @property
    def has_non_fatal_error(self):
        return False if self.__non_fatal_error is None else True
    
    @property
    def non_fatal_error(self):
        return self.__non_fatal_error
