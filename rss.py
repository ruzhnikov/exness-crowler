
# -*- coding: utf-8 -*-


import feedparser
from .response import CrawlerResponse


SAX_EXC_CLS = 'SAXParseException'


class RssLoad():
    """Класс для загрузки ресурсов с RSS"""
    def __init__(self, header_handler=None, items_handler=None):
        # задаём обработчики по умолчанию
        if header_handler is None:
            header_handler = self.__default_header_handler

        if items_handler is None:
            items_handler = self.__default_items_handler
        
        self._feed = header_handler
        self._items = items_handler
    
    def process(self, url):
        """Загрузка данных с ресурса"""

        feed_data = feedparser.parse(url)

        # храним нефатальную ошибку локально
        non_fatal_error = None
        if feed_data.bozo == 1:
            except_handler = _HandlerFeedExceptions(feed_data.bozo_exception)

            # если ошибка не фатальная, значит можем продолжать работать
            if except_handler.has_fatal_error:
                return CrawlerResponse(fatal_error=except_handler.error_message)
            
            non_fatal_error = except_handler.error_message

        try :
            for item in feed_data.entries:
                self._items(item)
        except Exception as e:
            return CrawlerResponse(fatal_error=e,
                                    non_fatal_error=non_fatal_error)
        
        return CrawlerResponse(non_fatal_error=non_fatal_error)

    def __default_header_handler(self, feed):
        print("Header: ")
        print(feed.title)

    def __default_items_handler(self, item):
        print("Item: ")
        print(item.title)
        print(item.pub_date)
        print(item.body)


class _HandlerFeedExceptions():
    """Класс для обработки ошибок парсера rss ресурсов"""

    def __init__(self, o_exception):
        self.has_fatal_error = False
        self.error_message = None
        self._handle(o_exception)

    def _handle(self, o_exception):
        cls_name = type(o_exception).__name__
        if cls_name == SAX_EXC_CLS:
            self.has_fatal_error = True

        self.error_message = o_exception.args[0]
