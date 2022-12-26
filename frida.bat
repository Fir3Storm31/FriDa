@echo off
if "%1" == "website" (
    "%CD%\env\Scripts\python.exe" "%CD%\FriDa\website.py"
) else if "%1" == "fridash" (
    "%CD%\env\Scripts\python.exe" "%CD%\FriDa\fridash.py"
) else if "%1" == "help" (
    type "%CD%\FriDa\help.txt"
) else (
    echo "Usage: frida website|fridash"
)