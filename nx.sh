#!/bin/sh
cd "$(dirname "$0")"
python -I -X utf8 check.py . $1; sed -n "2,400p" chunks/c$2.json
