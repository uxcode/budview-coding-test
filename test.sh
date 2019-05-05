#!/bin/bash

source ./venv/bin/activate
cd ./src
python -m unittest -v test.test_matcher
