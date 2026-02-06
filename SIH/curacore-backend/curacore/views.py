"""
Basic views for the CuraCore project.
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Simple health check endpoint to verify the API is running.
    """
    return Response({
        'status': 'healthy',
        'message': 'CuraCore API is running',
        'version': '1.0.0',
        'debug': settings.DEBUG
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_info(request):
    """
    API information endpoint.
    """
    return Response({
        'name': 'CuraCore API',
        'description': 'Mental health and wellness application API',
        'version': '1.0.0',
        'documentation': {
            'swagger': '/api/docs/',
            'redoc': '/api/redoc/',
            'schema': '/api/schema/'
        },
        'features': [
            'JWT Authentication',
            'CORS Support',
            'Auto-generated API Documentation',
            'SQLite Database'
        ]
    }, status=status.HTTP_200_OK)