#!/usr/bin/python3
"""Advance API module"""
import requests

def number_of_subscribers(subreddit):
    """Get the number of subscribers for a subreddit"""
    try:
        headers = {'User-Agent': '0x16-api_advanced:project: v1.0.0 (by /u/Moh\'King Yaga'}
        with requests.Session() as session:
            count = session.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)
        count.raise_for_status()
        return count.json().get('data', {}).get('subscribers', 0)
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return 0
    