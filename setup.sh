#!/usr/bin/env bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo 'Please execute this in python virtual environment!'
    exit 1
fi

pip install -r requirements.txt 1>/dev/null
pip install . 1>/dev/null
