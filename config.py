#!/usr/bin/env python3
"""
Configuration module for Sweet James Dashboard
Centralizes all configuration management including Azure EntraID settings
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Base configuration class"""
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'sweet-james-2025')
    
    # Environment
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DEBUG = ENVIRONMENT == 'development'
    PORT = int(os.getenv('PORT', 5000))
    
    # Google Ads API Configuration
    GOOGLE_ADS_DEVELOPER_TOKEN = os.getenv('GOOGLE_ADS_DEVELOPER_TOKEN')
    GOOGLE_ADS_CLIENT_ID = os.getenv('GOOGLE_ADS_CLIENT_ID')
    GOOGLE_ADS_CLIENT_SECRET = os.getenv('GOOGLE_ADS_CLIENT_SECRET')
    GOOGLE_ADS_REFRESH_TOKEN = os.getenv('GOOGLE_ADS_REFRESH_TOKEN')
    GOOGLE_ADS_CUSTOMER_IDS = os.getenv('GOOGLE_ADS_CUSTOMER_IDS', '').split(',')
    GOOGLE_ADS_MCC_ID = os.getenv('GOOGLE_ADS_MCC_ID')
    
    # Salesforce/Litify Configuration
    LITIFY_USERNAME = os.getenv('LITIFY_USERNAME')
    LITIFY_PASSWORD = os.getenv('LITIFY_PASSWORD')
    LITIFY_SECURITY_TOKEN = os.getenv('LITIFY_SECURITY_TOKEN')
    
    # Azure EntraID Configuration
    AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
    AZURE_CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')
    AZURE_TENANT_ID = os.getenv('AZURE_TENANT_ID')
    AZURE_AUTHORITY = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}" if AZURE_TENANT_ID else None
    AZURE_REDIRECT_URI = os.getenv('AZURE_REDIRECT_URI', 'http://localhost:5000/auth/callback')
    
    # Azure scopes for the application
    AZURE_SCOPES = ["User.Read"]  # Minimal scope to read user profile
    
    @property
    def azure_configured(self):
        """Check if Azure EntraID is properly configured"""
        return all([
            self.AZURE_CLIENT_ID,
            self.AZURE_CLIENT_SECRET, 
            self.AZURE_TENANT_ID
        ])
    
    @property
    def google_ads_configured(self):
        """Check if Google Ads API is properly configured"""
        return all([
            self.GOOGLE_ADS_DEVELOPER_TOKEN,
            self.GOOGLE_ADS_CLIENT_ID,
            self.GOOGLE_ADS_CLIENT_SECRET,
            self.GOOGLE_ADS_REFRESH_TOKEN
        ])
    
    @property
    def litify_configured(self):
        """Check if Litify/Salesforce is properly configured"""
        return all([
            self.LITIFY_USERNAME,
            self.LITIFY_PASSWORD,
            self.LITIFY_SECURITY_TOKEN
        ])

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    AZURE_REDIRECT_URI = 'http://localhost:5000/auth/callback'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    # Azure redirect URI should be set via environment variable in production

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get the appropriate configuration based on ENVIRONMENT"""
    env = os.getenv('ENVIRONMENT', 'development')
    return config.get(env, config['default'])