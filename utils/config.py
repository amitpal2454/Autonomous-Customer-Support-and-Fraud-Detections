# Auto-generated
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # App
    app_name: str = "Customer AI System"
    env: str = "development"

    # Azure OpenAI
    azure_openai_endpoint: str
    azure_openai_api_key: str
    azure_openai_deployment: str

    # Azure AI Search
    azure_search_endpoint: str
    azure_search_key: str
    azure_search_index: str

    # Azure SQL / Cosmos
    cosmos_endpoint: str
    cosmos_key: str
    cosmos_db_name: str

    # Redis
    redis_host: str
    redis_port: int = 6379

    # ML Endpoint
    azure_ml_endpoint: str
    azure_ml_key: str

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()