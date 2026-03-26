from langchain_openai import AzureChatOpenAI
from utils.config import get_settings

settings = get_settings()

llm = AzureChatOpenAI(
    azure_endpoint=settings.azure_openai_endpoint,
    api_key=settings.azure_openai_api_key,
    deployment_name=settings.azure_openai_deployment,
    temperature=0
)