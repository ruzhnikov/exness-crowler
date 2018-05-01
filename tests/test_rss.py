# -*- coding: utf-8 -*-


import pytest
from exness.rss import RssLoad
from exness.crawler import Crawler


FEED_DATA = dict()
ITEM_DATA = dict()
ITEM_MANDATORY_FIELDS = ("title", "link", "published", "description")


def read_rss(simple=True):
    fname = "simple_rss.xml" if simple else "complex_rss.xml"
    rss = None
    with open("tests/" + fname) as f:
        rss = f.read()
    
    return rss

def collect_feed_data():
    local_fd = FEED_DATA
    def local_data(feed):
        local_fd["title"] = feed.title
    
    return local_data

def collect_item():
    local_item = ITEM_DATA
    def local_data(item):
        for key in ITEM_MANDATORY_FIELDS:
            local_item[key] = item.get(key)
    
    return local_data

def clear_data():
    FEED_DATA.clear()
    ITEM_DATA.clear()

def get_crawler():
    clear_data()
    feed_handler = collect_feed_data()
    item_handler = collect_item()
    rss_object = RssLoad(feed_handler, item_handler)
    crawler = Crawler(rss_object)

    return crawler


def test_simple_rss():
    crawler = get_crawler()

    rawdata = read_rss(simple=True)
    result = crawler.process(rawdata)

    assert result.success is True
    assert len(FEED_DATA) > 0
    assert "title" in FEED_DATA
    assert FEED_DATA.get("title") == "Sample Feed"
    assert len(ITEM_DATA) == 0

def test_complex_rss():
    crawler = get_crawler()

    rawdata = read_rss(simple=False)
    result = crawler.process(rawdata)

    assert result.success is True
    assert len(FEED_DATA) > 0
    assert FEED_DATA.get("title") == "Sample Feed"
    assert len(ITEM_DATA) > 0
    assert ITEM_DATA.get("title") == "To be or not to be?"
    assert ITEM_DATA.get("description") == "Not to be"

