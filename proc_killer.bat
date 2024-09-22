@echo off
start /min pythonw "%~dp0monitor.py"
if %ERRORLEVEL% neq 0 (
    echo An error occurred while running the script. Error code: %ERRORLEVEL%
    pause
) else (
    echo Script is running minimized.
)
