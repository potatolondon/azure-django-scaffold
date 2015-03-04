#!/bin/sh

pip install -r requirements/local.txt

ln -s dev-only-package.json package.json
npm install
