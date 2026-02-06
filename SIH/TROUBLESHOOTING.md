# CuraCore Troubleshooting Guide

## Common Issues and Solutions

### 1. CORS Errors (Failed to fetch)

**Error**: `Access to fetch at 'http://localhost:8000/...' has been blocked by CORS policy`

**Solutions**:
1. **Make sure backend is running**:
   ```bash
   cd backend
   python start.py
   ```

2. **Check server status**:
   ```bash
   cd backend
   python check_server.py
   ```

3. **Verify server is accessible**:
   - Open http://localhost:8000/health in your browser
   - Should show: `{"status": "healthy", ...}`

### 2. Backend Won't Start

**Error**: `ModuleNotFoundError` or import errors

**Solutions**:
1. **Run the installer**:
   ```bash
   cd backend
   python install.py
   ```

2. **Install dependencies manually**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Check Python version** (requires Python 3.8+):
   ```bash
   python --version
   ```

### 3. AI Service Issues

**Error**: AI responses not working or model loading errors

**Solutions**:
1. **Use Lite Mode** (recommended for quick start):
   - Delete `.env` file in backend folder
   - Run `python install.py` and choose option 1

2. **For Full AI Mode**:
   - Ensure you have enough disk space (~2GB)
   - Run `python setup_models.py` to download models
   - Check internet connection for model downloads

### 4. Authentication Errors

**Error**: `401 Unauthorized` or login issues

**Solutions**:
1. **Clear browser storage**:
   - Open browser dev tools (F12)
   - Go to Application/Storage tab
   - Clear localStorage for localhost:3000

2. **Check token expiration**:
   - Tokens expire after 30 minutes
   - Simply log in again

### 5. Database Issues

**Error**: Database connection or SQLite errors

**Solutions**:
1. **Delete and recreate database**:
   ```bash
   cd backend
   rm users.db
   python start.py  # Will recreate database
   ```

2. **Check file permissions**:
   - Ensure backend folder is writable
   - Check users.db file permissions

### 6. React Router Warnings

**Warning**: Future flag warnings in console

**Solution**: These are just warnings and don't affect functionality. They're already fixed in the latest code.

## Quick Diagnostic Commands

### Check Everything:
```bash
# 1. Check backend
cd backend
python check_server.py

# 2. Check frontend
cd ..
npm start

# 3. Test API manually
curl http://localhost:8000/health
```

### Reset Everything:
```bash
# Backend reset
cd backend
rm users.db .env
python install.py

# Frontend reset
cd ..
rm -rf node_modules package-lock.json
npm install
npm start
```

## Getting Help

If you're still having issues:

1. **Check the console logs** in both terminal and browser
2. **Verify all services are running**:
   - Backend: http://localhost:8000/health
   - Frontend: http://localhost:3000
3. **Try the lite mode** if full AI mode is causing issues
4. **Check your firewall/antivirus** isn't blocking localhost connections

## Port Conflicts

If ports 3000 or 8000 are in use:

**Frontend** (change React port):
```bash
PORT=3001 npm start
```

**Backend** (change API port):
```bash
# Edit .env file:
API_PORT=8001
```

Then update `API_BASE_URL` in frontend files to match the new port.