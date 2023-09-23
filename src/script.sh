#!/bin/sh
nix-shell -p pipenv --run "pipenv install Jinja2 && code ."
