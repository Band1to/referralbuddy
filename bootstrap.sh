#!/bin/bash

virtualenv --distribute venv
source venv/bin/activate
LA="$HOME/.mytemplates/.local.autorun"
if [ -f "$LA" ]; then
    cp "$LA" .
fi
pip install --download-cache=~/.pip_cache --log=log/pip.log -r requirements.txt
