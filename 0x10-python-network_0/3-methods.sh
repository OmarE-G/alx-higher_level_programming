#!/bin/bash
# DELETE
curl -si "$1" -X "OPTIONS" | grep -i 'allow:' | cut -d ' ' -f 2
