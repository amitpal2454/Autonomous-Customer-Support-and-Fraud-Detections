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
    azure_storage_connection_string:str

    azure_openai_embedding_endpoint:str
    azure_openai_embedding_api_key:str
    azure_openai_embedding_deployment:str

    # Pinecone
    pinecone_api_key:str
    pinecone_index:str
 
    # Redis
    redis_host: str
    redis_port: int = 6379

    # ML Endpoint
    #azure_ml_endpoint: str
    #azure_ml_key: str

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()