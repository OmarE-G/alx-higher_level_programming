#!/usr/bin/python3
'''api request'''
import requests
import sys
from requests.exceptions import JSONDecodeError as JDE


if __name__ == '__main__':
    query = ""
    if len(sys.argv) > 1:
        query = sys.argv[1]
    data = {'q': query}
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        print(f"[{r.json()['id']}] {r.json()['name']}")

    except JDE:
        print("Not a valid JSON")

    except KeyError:
        print("No result")
