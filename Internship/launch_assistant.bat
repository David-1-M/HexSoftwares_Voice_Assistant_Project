@echo off
echo Loading modules...
call assistant-env\Scripts\activate.bat
echo System initialized. Launching assistant now...
python "Virtual Assistant.py"
echo.
echo Assistant session ended. Goodbye!
pause
