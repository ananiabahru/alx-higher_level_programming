#!/bin/bash
# the size of the body of the response
curl -sI "$1" | grep -oiE '
content-length: [0-9]+' | cut -d ' ' -f2
