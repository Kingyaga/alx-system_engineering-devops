#!/usr/bin/python3
""" Advance API module """

import requests

def number_of_subscribers(subreddit):
    """ Get number of subscribers for a subreddit """
    try:
        headers = {
            'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/Moh\'King Yaga'
        }
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get('data', {}).get('subscribers', 0)
    except requests.RequestException as e:
        return 0
