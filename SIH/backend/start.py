#!/usr/bin/env python3
"""
Start script for CuraCore Backend
"""
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    # Print configuration
    ai_mode = os.getenv("AI_SERVICE_MODE", "lite")
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    
    print("🤖 Starting CuraCore Backend")
    print("=" * 40)
    print(f"AI Service Mode: {ai_mode.upper()}")
    print(f"Server: http://{host}:{port}")
    print(f"API Docs: http://{host}:{port}/docs")
    print("=" * 40)
    
    # Start server
    uvicorn.run(
        "main:app", 
        host=host, 
        port=port, 
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()