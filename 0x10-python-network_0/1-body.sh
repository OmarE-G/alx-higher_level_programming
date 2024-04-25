#!/bin/bash
# response body
R=$(curl "$1" -s  -o /dev/null -w %{http_code}); [ $R -eq 200 ] && curl -s "$1"
