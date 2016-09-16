#!/bin/bash

# This script clones from the original repository and creates two necessary files:
# config.h and src/xrayglob_inline.c
# config.h may be system dependent but __seems__ not contain real OS dependent information -> to be checked!

# On ubuntu 14.04 using python3
# sudo apt-get install git autoconf libtool swig python3-devel

git clone https://github.com/tschoonj/xraylib.git

cd xraylib
autoreconf -i
# Next line will create config.h 
./configure
# Next line will create src/xrayglob_inline.c
make
cd ..
