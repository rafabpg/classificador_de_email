from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    Settings configuration class for application environment variables.
    Attributes:
        API_TOKEN (Optional[str]): Token used for API authentication. Loaded from environment variables if available.
        API_URL_CLASSIFIER (Optional[str]): URL for the classifier API endpoint. Defaults to HuggingFace BART MNLI model.
        API_URL_SUGGESTION (Optional[str]): URL for the suggestion API endpoint. Defaults to HuggingFace chat completions.
    Config:
        env_file (str): Specifies the environment file to load variables from (default: ".env").
        extra (str): Allows extra fields in the environment configuration (default: "allow").
    """
    
    API_TOKEN: str
    API_URL_CLASSIFIER: Optional[str] = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
    API_URL_SUGGESTION: Optional[str] = "https://router.huggingface.co/nebius/v1/chat/completions"
    DEBUG:bool = True
    CORS_ORIGINS: str = "*"

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
