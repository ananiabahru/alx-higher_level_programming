#!/bin/bash
#  Bash script that takes in URL the server will accept
curl -silk -X OPTIONS "$1" | grp -oiE '
Allow: .+' | cut -d ' ' -f2-
