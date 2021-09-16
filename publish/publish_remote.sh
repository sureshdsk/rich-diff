#!/usr/bin/env bash
python setup.py sdist bdist_wheel
python upload.py
python clean.py
