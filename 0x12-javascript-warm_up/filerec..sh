#!/bin/bash

filename=$1

# Check if filename is provided
if [ -z "$filename" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Check if file exists
if [ ! -f "$filename" ]; then
    echo "File $filename not found."
    exit 1
fi

# Read each line (domain) from the file
while IFS= read -r domain; do
    echo "Processing domain: $domain"

    # Run your commands for each domain
    subfinder -d "$domain" | httpx -sc | grep "200" | grep -oP ".*?(?=\s)" > "${domain}_subds.txt"
    paramspider -s -l "${domain}_subds.txt" | kxss | grep "<" >> "xss.txt"

    echo "Finished processing domain: $domain"
done < "$filename"
