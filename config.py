import os

class Config:
    # Azure AD Configuration
    AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
    AZURE_CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')
    AZURE_TENANT_ID = os.getenv('AZURE_TENANT_ID')
    
    # Derived Azure settings
    azure_authority = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}"
    AZURE_SCOPE = ["User.Read"]
    AUTH_REDIRECT_URI = "https://ppcdash-hbk4fbbkeuebb5hv.westus3-01.azurewebsites.net/getAToken"