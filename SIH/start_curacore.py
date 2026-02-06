#!/usr/bin/env python3
"""
Complete startup script for CuraCore application
Checks dependencies, starts backend, and provides frontend instructions
Windows-safe, cross-platform, production-ready
"""

import os
import sys
import subprocess
import time
import threading
from pathlib import Path

# ------------------ UI HELPERS ------------------

def print_banner():
    print("=" * 50)
    print("CuraCore Application Startup")
    print("=" * 50)

# ------------------ CHECKS ------------------

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info

    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"ERROR: Python {version.major}.{version.minor} detected")
        print("CuraCore requires Python 3.8 or higher")
        return False

    print(f"OK: Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_backend_setup():
    """Check if backend is properly set up"""
    backend_path = Path("backend")

    if not backend_path.exists():
        print("ERROR: Backend folder not found")
        return False

    requirements_file = backend_path / "requirements.txt"
    if not requirements_file.exists():
        print("ERROR: backend/requirements.txt not found")
        return False

    print("OK: Backend folder structure")
    return True


def check_frontend_setup():
    """Check if frontend is properly set up (non-blocking)"""
    package_json = Path("package.json")
    node_modules = Path("node_modules")

    if not package_json.exists():
        print("WARNING: Frontend package.json not found")
        return False

    if not node_modules.exists():
        print("WARNING: Node modules not installed")
        print("Run: npm install")
        return False

    print("OK: Frontend setup")
    return True

# ------------------ BACKEND INSTALL ------------------

def install_backend_dependencies():
    """Install backend dependencies"""
    print("Installing backend dependencies...")

    original_dir = os.getcwd()

    try:
        os.chdir("backend")

        if Path("install.py").exists():
            print("Running guided backend installation...")

            process = subprocess.Popen(
                [sys.executable, "install.py"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate(input="1\n")

            if process.returncode == 0:
                print("OK: Backend dependencies installed")
                return True
            else:
                print("ERROR: Backend installation failed")
                print(stderr)
                return False
        else:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
            ])
            print("OK: Backend dependencies installed")
            return True

    except subprocess.CalledProcessError as e:
        print(f"ERROR: Dependency installation failed: {e}")
        return False
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        return False
    finally:
        os.chdir(original_dir)

# ------------------ BACKEND SERVER ------------------

def start_backend_server():
    """Start the backend server in a background thread"""

    def run_server():
        original_dir = os.getcwd()
        try:
            os.chdir("backend")
            subprocess.run([sys.executable, "start.py"])
        except Exception as e:
            print(f"ERROR: Backend server crashed: {e}")
        finally:
            os.chdir(original_dir)

    print("Starting backend server...")

    server_thread = threading.Thread(
        target=run_server,
        daemon=True
    )
    server_thread.start()

    time.sleep(3)

    try:
        original_dir = os.getcwd()
        os.chdir("backend")

        result = subprocess.run(
            [sys.executable, "check_server.py"],
            capture_output=True,
            text=True
        )

        os.chdir(original_dir)

        if result.returncode == 0:
            print("OK: Backend server is running")
            return True
        else:
            print("ERROR: Backend server failed to start")
            print(result.stdout)
            return False

    except Exception as e:
        print(f"ERROR: Could not verify backend status: {e}")
        return False

# ------------------ INSTRUCTIONS ------------------

def print_next_steps():
    print("\nBackend is ready")
    print("=" * 50)
    print("To start the frontend:")
    print("1. Open a new terminal")
    print("2. Run: npm start")
    print("3. Open: http://localhost:3000")
    print()
    print("Backend URLs:")
    print("- API:    http://localhost:8000")
    print("- Health: http://localhost:8000/health")
    print("- Docs:   http://localhost:8000/docs")
    print()
    print("To stop the backend:")
    print("Press Ctrl+C in this terminal")
    print("=" * 50)

# ------------------ MAIN ------------------

def main():
    print_banner()

    if not check_python_version():
        return False

    if not check_backend_setup():
        return False

    check_frontend_setup()  # Non-blocking

    # Check if backend deps already exist
    try:
        os.chdir("backend")
        import fastapi  # noqa
        print("OK: Backend dependencies already installed")
        os.chdir("..")
    except ImportError:
        os.chdir("..")
        if not install_backend_dependencies():
            return False

    if not start_backend_server():
        return False

    print_next_steps()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down CuraCore...")
        return True


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\nStartup failed: {e}")
        sys.exit(1)