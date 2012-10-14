#!/bin/bash

cd $HOME/projects/latex-to-unicode

if [ "$1" == "--gui" ]; then
    text=$(./gui.py)
else
    text=$(python ./convert.py <<< "$@")
fi

if test -z "$text"; then
	exit
fi
echo -n "$text" | xclip
echo -n "$text" | xclip -selection clipboard
xdotool key shift+Insert
