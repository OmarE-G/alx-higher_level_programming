#!/bin/bash
# response body size
curl "$1" -si  | grep -i 'Content-Length' | cut -d ' ' -f 2

