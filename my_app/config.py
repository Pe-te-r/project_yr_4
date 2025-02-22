# my_app/config.py

class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True
    # Add other configuration variables as needed

class ProductionConfig(Config):
    DEBUG = False
    # Add production-specific configurations

class DevelopmentConfig(Config):
    DEBUG = True
    # Add development-specific configurations