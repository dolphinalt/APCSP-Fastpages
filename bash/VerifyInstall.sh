#!/bin/bash

runcmd="$1 install $2"
read -p "[VerifyInstall] Are you sure you want to install $2? [Y/n] " confirm

if [[ $confirm == "y" || $confirm == "Y" ]]; then 
    echo "[VerifyInstall] Running [$runcmd]..."
    eval $runcmd
    echo "Brew package list:"
    brew list | grep --color -iw $2
else
    echo "[VerifyInstall] INSTALL FAILED, CANCLED BY USER"
    exit 1
fi