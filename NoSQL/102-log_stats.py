#!/usr/bin/env python3
"""Display Nginx log statistics and the ten most frequent IPs."""

from pymongo import MongoClient


def print_log_stats(nginx_collection):
    """Print request statistics followed by the ten most common IPs."""
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")

    for method in ("GET", "POST", "PUT", "PATCH", "DELETE"):
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_count))
    print("IPs:")

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
    ]
    for item in nginx_collection.aggregate(pipeline):
        print("\t{}: {}".format(item.get("_id"), item.get("count")))


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_log_stats(client.logs.nginx)
    client.close()
