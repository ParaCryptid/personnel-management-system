@echo off
set APP_NAME=personnel-management-system
set VERSION=1.0.0

:: Clean previous builds
rmdir /S /Q build\%APP_NAME% 2>nul
mkdir build\%APP_NAME%

:: Create virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt
pip install pyinstaller

:: Build the executable
pyinstaller --onefile app.py --name %APP_NAME%_win

:: Move to build directory
move dist\%APP_NAME%_win.exe build\%APP_NAME%\%APP_NAME%_win.exe

echo Build complete. Output is in build\%APP_NAME%
