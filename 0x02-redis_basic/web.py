#!/usr/bin/env python3
"""
 Implementing an expiring web cache and tracker
"""
import requests
import redis
from typing import Callable
from functools import wraps

re = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """ Decorator to know the number of calls """

    @wraps(method)
    def wrapper(url):
        """ the wrapper decorator """
        re.incr(f"count:{url}")
        cached_html = re.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        re.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


def get_page(url: str) -> str:
    """ obtain the HTML content of a given URL and return it"""
    req = requests.get(url)

    return req.text
