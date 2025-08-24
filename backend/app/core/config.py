from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    Settings configuration class for application environment variables.
    Attributes:
        API_TOKEN (str): Token used for API authentication.
        API_URL (Optional[str]): URL endpoint for the API. Defaults to "https://router.huggingface.co/nebius/v1/chat/completions".
        DEBUG (bool): Flag to enable or disable debug mode. Defaults to True.
        CORS_ORIGINS (str): Allowed origins for CORS. Defaults to "*".
    Config:
        env_file (str): Path to the environment file. Defaults to ".env".
        extra (str): Specifies handling of extra fields. Set to "allow".
    """

    
    API_TOKEN: str
    API_URL: Optional[str] = "https://router.huggingface.co/nebius/v1/chat/completions"
    DEBUG: Optional[bool] = True
    CORS_ORIGINS: Optional[str] = "*"

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
