REM @echo off

openfiles > nul
if errorlevel 1 (
    PowerShell.exe -Command Start-Process \"%~f0\" -Verb runas
    exit
)

set TARGET_DIR=crash3

cd /d %~dp0
MKLINK /D ..\Archipelago\worlds\%TARGET_DIR% .\%TARGET_DIR%
pause