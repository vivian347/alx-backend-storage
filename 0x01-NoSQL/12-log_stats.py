#!/usr/bin/env python3

""" 12-logs"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    count_docs = nginx_collection.count_documents({})
    print(f"{count_docs} logs")
    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for item in method:
        method_count = nginx_collection.count_documents({"method": item})
        print(f"\tmethod {item}: {method_count}")

    GET_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{GET_count} status check")
