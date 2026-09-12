#!/usr/bin/env python3
"""Display summary statistics for Nginx request logs in MongoDB."""

from pymongo import MongoClient


def print_log_stats(nginx_collection):
    """Print log totals, HTTP method counts, and status-check count."""
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")

    for method in ("GET", "POST", "PUT", "PATCH", "DELETE"):
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_count))


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_log_stats(client.logs.nginx)
    client.close()
