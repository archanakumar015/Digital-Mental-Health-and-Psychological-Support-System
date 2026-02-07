@echo off
echo Testing Django configuration...
python manage.py check --deploy
if %errorlevel% equ 0 (
    echo Django configuration is valid!
) else (
    echo Django configuration has issues.
)
pause