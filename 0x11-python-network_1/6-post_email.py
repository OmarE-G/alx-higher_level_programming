#!/usr/bin/python3
'''script to fetch a url'''
import requests
import sys


if __name__ == '__main__':
    '''post request'''
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    print(requests.post(url, data=data).text)
