#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
from redis.client import Redis
import requests


redis = Redis()
count = 0


def get_page(url: str) -> str:
    """
    uses the requests module to obtain
    the HTML content of a particular URL and returns it.
    """
    data = f"count:{url}"
    redis.set(data, count)
    res = requests.get(url)
    redis.incr(data)
    redis.setex(data, 10, redis.get(data))
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
