#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    method_stat = {'GET': 0, 'POST': 0, 'PUT': 0, 'PATCH': 0, 'DELETE': 0}
    status_check_count = 0
    logs = []
    for log in nginx_collection.find():
        logs.append(log)

    for log in logs:
        if log["method"] in method_stat.keys():
            method_stat[log["method"]] += 1

        if log["path"] == "/status":
            status_check_count += 1

    # print log count
    print(f"{len(logs)} logs")

    # print method stats
    print("Methods:")
    for key, val in method_stat.items():
        print(f"\tmethod {key}: {val}")

    # print status_check count
    print(f"{status_check_count} status check")
