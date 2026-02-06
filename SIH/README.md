# 🤖 CuraCore - AI-Powered Mental Health Companion

A comprehensive mental health application with AI-powered chatbot, mood tracking, and wellness features.

## ✨ Features

- **🤖 AI Chatbot**: Emotion-aware conversational AI with pretrained models
- **📊 Mood Tracking**: Real-time emotion detection and mood analytics
- **📈 Dashboard**: Personalized insights and progress tracking
- **🔐 Authentication**: Secure user accounts with JWT tokens
- **💾 Data Storage**: SQLite database for all user data

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
```bash
python start_curacore.py
```
This will:
- Check system requirements
- Install backend dependencies
- Start the backend server
- Provide frontend startup instructions

### Option 2: Manual Setup

#### Backend Setup:
```bash
cd backend
python install.py  # Choose option 1 for quick start
python start.py
```

#### Frontend Setup:
```bash
npm install
npm start
```

## 📋 Requirements

- **Python**: 3.8 or higher
- **Node.js**: 14 or higher
- **npm**: 6 or higher

## 🔧 Configuration

The backend supports two AI modes:

### 🚀 Lite Mode (Default)
- Fast startup (~30 seconds)
- Keyword-based emotion detection
- Rule-based responses
- Small memory footprint

### 🧠 Full AI Mode
- Advanced pretrained models
- Real emotion detection
- AI-generated responses
- Requires ~2GB disk space

## 📱 Usage

1. **Start the application** using one of the methods above
2. **Open your browser** to http://localhost:3000
3. **Register/Login** to create your account
4. **Start chatting** with the AI companion
5. **Track your mood** and view insights

## 🌐 API Endpoints

- `http://localhost:8000` - API root
- `http://localhost:8000/docs` - Interactive API documentation
- `http://localhost:8000/health` - Health check

## 🛠️ Troubleshooting

### Common Issues:

**CORS Errors**: Make sure backend is running on port 8000
```bash
cd backend
python check_server.py
```

**Dependencies Issues**: Run the installer
```bash
cd backend
python install.py
```

**Port Conflicts**: Change ports in configuration
```bash
# Frontend
PORT=3001 npm start

# Backend (edit .env file)
API_PORT=8001
```

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed solutions.

## 📁 Project Structure

```
curacore/
├── backend/                 # FastAPI backend
│   ├── ai_service.py       # Full AI service (pretrained models)
│   ├── ai_service_lite.py  # Lightweight AI service
│   ├── main.py             # FastAPI application
│   ├── database.py         # SQLite database operations
│   ├── auth.py             # JWT authentication
│   ├── install.py          # Guided installation
│   └── start.py            # Server startup script
├── src/                    # React frontend
│   ├── pages/              # Application pages
│   ├── components/         # Reusable components
│   └── contexts/           # React contexts
├── start_curacore.py       # Complete startup script
└── README.md               # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter issues:

1. Check the [troubleshooting guide](TROUBLESHOOTING.md)
2. Verify all services are running
3. Check console logs for errors
4. Try the lite mode if full AI mode fails

---

**Happy chatting! 🎉**