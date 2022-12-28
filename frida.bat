@echo off
if "%1" == "-env" (
    if "%2" == "website" (
        "%CD%\FriDa\env\Scripts\python.exe" "%CD%\FriDa\website.py"
    ) else if "%2" == "fridash" (
        "%CD%\FriDa\env\Scripts\python.exe" "%CD%\FriDa\fridash.py"
    ) else (
        echo I comandi e/o le opzioni che hai inserito non sono validi.
        echo Usa frida -help per visualizzare la lista dei comandi.
    )
) else if "%1" == "website" (
    "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python39\python.exe" "%CD%\FriDa\website.py"
) else if "%1" == "fridash" (
    "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python39\python.exe" "%CD%\FriDa\fridash.py" 
) else if "%1" == "-help" (
    type "%CD%\FriDa\help.txt"
) else (
    echo I comandi e/o le opzioni che hai inserito non sono validi.
    echo Usa frida -help per visualizzare la lista dei comandi.
)