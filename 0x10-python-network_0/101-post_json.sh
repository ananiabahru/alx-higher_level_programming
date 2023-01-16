#!/bin/bash
# sends a JSON POST request to a URL pasd as a second argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"


