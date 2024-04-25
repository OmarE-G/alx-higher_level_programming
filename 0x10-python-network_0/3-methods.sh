#!/bin/bash
# DELETE
curl -siL "$1" -X "OPTIONS" | grep 'allow:' | cut -d ' ' -f 2
