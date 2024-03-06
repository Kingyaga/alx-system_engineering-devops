#!/usr/bin/python3
"""
Module for querying the Reddit API for a given subreddit's subscriber count.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "0x16-api_advanced:project: v1.0.0 (by /u/Moh'King Yaga)"}

    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return 0

    try:
        data = response.json()
        return data["data"]["subscribers"]
    except (ValueError, KeyError):
        return 0