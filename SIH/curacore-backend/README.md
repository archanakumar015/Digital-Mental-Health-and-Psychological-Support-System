# CuraCore Backend

Django REST API backend for the CuraCore mental health and wellness application.

## Features

- **JWT Authentication**: Secure token-based authentication using djangorestframework-simplejwt
- **CORS Support**: Configured for frontend integration with django-cors-headers
- **API Documentation**: Auto-generated OpenAPI documentation with drf-spectacular
- **SQLite Database**: Pre-configured for development with easy migration to PostgreSQL for production

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Configuration**:
   - Copy `.env.example` to `.env`
   - Update the environment variables as needed

3. **Database Setup**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/

## Project Structure

```
curacore-backend/
├── curacore/           # Main Django project
│   ├── __init__.py
│   ├── settings.py     # Django settings with JWT, CORS, API docs
│   ├── urls.py         # Main URL configuration
│   ├── wsgi.py         # WSGI application
│   └── asgi.py         # ASGI application
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md          # This file
```

## Configuration Details

### JWT Authentication
- Access token lifetime: 15 minutes
- Refresh token lifetime: 7 days
- Automatic token rotation enabled

### CORS Settings
- Configured for React development server (localhost:3000)
- Credentials support enabled

### Database
- SQLite3 for development
- Easy migration to PostgreSQL for production

## Next Steps

This foundation is ready for:
1. Creating Django apps for specific features (users, quizzes, mood tracking, etc.)
2. Implementing API endpoints
3. Adding custom authentication and authorization logic
4. Integrating with the React frontend