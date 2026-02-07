# CuraCore Django Backend Setup Script

Write-Host "Setting up CuraCore Django backend..." -ForegroundColor Green
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Python not found. Please install Python first." -ForegroundColor Red
    exit 1
}

# Run makemigrations
Write-Host "Step 1: Making migrations..." -ForegroundColor Yellow
python manage.py makemigrations
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: makemigrations failed" -ForegroundColor Red
    exit 1
}

# Run migrate
Write-Host "Step 2: Running migrations..." -ForegroundColor Yellow
python manage.py migrate
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: migrate failed" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "✓ Database setup complete!" -ForegroundColor Green
Write-Host "You can now run: python manage.py runserver" -ForegroundColor Cyan