#!/bin/bash
#  Bash script that takes in URL the server will accept
curl -silk -X OPTIONS "$1" | grep -oiE '
Allow: .+' | cut -d ' ' -f2-
