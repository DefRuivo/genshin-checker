#!/bin/bash

genshindb=https://github.com/theBowja/genshin-db

if [ ! -d "genshin-db" ]; then
    git clone $genshindb
else
    cd genshin-db
    git remote add upstream $genshindb
    git fetch upstream
    git pull origin main
fi