#!/usr/bin/env bash
python setup.py sdist bdist_wheel && pip install dist/*.whl
python clean.py
