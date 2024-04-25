#!/bin/bash
# DELETE
curl -siL "$1" -X "OPTIONS" | grep -i 'allow:' | cut -d ' ' -f 2
