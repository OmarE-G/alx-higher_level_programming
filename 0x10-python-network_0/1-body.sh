#!/bin/bash
# response body
R=$(curl "$1" -sL  -o /dev/null -w %{http_code}); [ $R -eq 200 ] && curl -sL "$1"
