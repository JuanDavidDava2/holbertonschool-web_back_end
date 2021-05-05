#!/usr/bin/env python3
"""
    Write a Python function that returns
    the list of school having a specific topic
"""
from pymongo import MongoClient


def logger(a: dict) -> int:
    """return logger"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    return nginx_logs.count_documents(a)


def main():
    """
    Nginx logs stored in MongoDB
    """
    print(f"{ logger({}) } logs")
    print("Methods:")
    print(f"\tmethod GET: { logger({'method': 'GET'}) }")
    print(f"\tmethod POST: { logger({'method': 'POST'}) }")
    print(f"\tmethod PUT: {logger({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {logger({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {logger({'method': 'DELETE'})}")
    print(f"{logger({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()
