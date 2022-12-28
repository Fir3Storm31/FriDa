#!/bin/bash
if [ $1 == '-env' ]
then
    if [ $2 == 'website' ]
    then
        source env/bin/activate
        python FriDa/website.py
    elif [ $2 == 'fridash' ]
    then
        source env/bin/activate
        python FriDa/fridash.py
    else
        echo I comandi e/o le opzioni che hai inserito non sono validi.
        echo Usa frida -help per visualizzare la lista dei comandi.
elif [ $1 == 'website' ]
then
    python FriDa/website.py
elif [ $1 == 'fridash' ]
then
    python FriDa/fridash.py
elif [ $1 == '-help' ]
then
    cat FriDa/help.txt
else
    echo I comandi e/o le opzioni che hai inserito non sono validi.
    echo Usa frida -help per visualizzare la lista dei comandi.
fi
