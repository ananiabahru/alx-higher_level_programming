#!/bin/bash
# sends a JSON POST request to a URL pasd as a second argument
curl -sL -X POST -H '
Content-Type: application/json' -d "$([-f "$2" ] && cat "$2")" "$1"


