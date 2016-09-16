#!/bin/bash

# This script modifies the original sources to enable distutils for python.

cp setup.py ./xraylib
cp MANIFEST.in ./xraylib
mv ./xraylib/src/xraylib.i ./xraylib
cp ./xraylib/python/xraylib.py ./xraylib
