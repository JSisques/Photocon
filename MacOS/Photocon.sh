#!/bin/sh
cd /usr/bin

git pull origin master https://github.com/JSisques/Photocon.git

cd Photocon/src

python3 main.py