@echo off
echo Setting up CuraCore Django backend...
echo.

echo Step 1: Making migrations...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo Error: makemigrations failed
    pause
    exit /b 1
)

echo Step 2: Running migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo Error: migrate failed
    pause
    exit /b 1
)

echo.
echo Database setup complete!
echo You can now run: python manage.py runserver
pause