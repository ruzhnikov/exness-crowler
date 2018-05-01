
# -*- coding: utf-8 -*-


import socket
import feedparser
from .response import CrawlerResponse


SAX_EXC_CLS = 'SAXParseException'
# Таймаут запроса
NETWORK_TIMEOUT = 10


class RssLoad():
    """Класс для загрузки ресурсов с RSS"""
    def __init__(self, feed_handler=None, item_handler=None):
        # задаём обработчики по умолчанию
        if feed_handler is None:
            feed_handler = self._default_feed_handler

        if item_handler is None:
            item_handler = self._default_item_handler

        self._feed = feed_handler
        self._items = item_handler

    def process(self, url):
        """Загрузка данных с ресурса"""

        socket.setdefaulttimeout(NETWORK_TIMEOUT)
        feed_data = feedparser.parse(url)

        # храним нефатальную ошибку локально
        warn = None
        if feed_data.bozo == 1:
            except_handler = _HandlerFeedExceptions(feed_data.bozo_exception)

            # если ошибка не фатальная, значит можем продолжать работать
            if except_handler.has_fatal_error:
                return CrawlerResponse(error=except_handler.error_message)

            warn = except_handler.error_message

        try :
            self._feed(feed_data.feed)
            for item in feed_data.entries:
                self._items(item)
        except Exception as e:
            return CrawlerResponse(error=e, warning=warn)
        
        return CrawlerResponse(warning=warn)

    def _default_feed_handler(self, feed):
        print("Header: {}".format(feed.title))

    def _default_item_handler(self, item):
        print("Item: ")
        print(item.title)
        print(item.link)
        print(item.published)
        print(item.description)


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
