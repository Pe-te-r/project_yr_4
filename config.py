import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
 

class Config:
    # Secret key for session management and security
    SECRET_KEY = os.getenv('SECRET_KEY', 'this-is-a-default-secret-key')

    # Debug mode (set to False in production)
    DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 't')

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to save resources

    # Flask-WTF configuration for CSRF protection
    WTF_CSRF_ENABLED = True

    # Email configuration (if you plan to send emails)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() in ('true', '1', 't')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@example.com')

    # File upload configuration (if you plan to handle file uploads)
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16 * 1024 * 1024))  # 16 MB limit

    # Session configuration
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False').lower() in ('true', '1', 't')
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # Add other configuration variables as needed

class ProductionConfig(Config):
    DEBUG = False
    # Production-specific configurations
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Use a production database URL
    SESSION_COOKIE_SECURE = True  # Ensure cookies are only sent over HTTPS in production

class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific configurations
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'  # Use a local SQLite database for development

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # Use an in-memory SQLite database for testing
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing