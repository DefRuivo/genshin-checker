#!/bin/bash

genshindb=https://github.com/theBowja/genshin-db

if [ "$color_prompt" = yes ]; then
    if git --version &>/dev/null; then
        # PS1 Line to show current Git Branch in the Prompt
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\[\033[01;32m\]$(__git_ps1 " (%s)")\[\033[00m\]\$ '
    else
        # Original PS1 Line
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    fi
else
    if git --version &>/dev/null; then
        # PS1 Line to show current Git Branch in the Prompt
        PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w $(__git_ps1 "(%s)")\$ '
    else
        # Original PS1 Line
            PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
    fi
fi

if [ ! -d "genshin-db" ]; then
    git clone $genshindb
else
    cd genshin-db
    git remote add upstream $genshindb
    git fetch upstream
    git pull origin main
fi