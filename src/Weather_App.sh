#!/bin/bash
FILE=.venv
if [ -d "$FILE" ]; then

else
    python3 -m venv .venv
    source .venv/bin/activate
fi

pip install -r requirements.txt

python3 src/main.py