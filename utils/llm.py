from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from utils.config import get_settings


settings = get_settings()

llm = AzureChatOpenAI(
    azure_endpoint=settings.azure_openai_endpoint,
    api_key=settings.azure_openai_api_key,
    deployment_name=settings.azure_openai_deployment,
    api_version="2024-12-01-preview",
    #api_version=settings.azure_openai_api_version,
    temperature=0.3
)



settings = get_settings()

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=settings.azure_openai_embedding_endpoint,
    api_key=settings.azure_openai_embedding_api_key,
    deployment=settings.azure_openai_embedding_deployment,
    #api_version=settings.azure_openai_api_version
)


def get_embedding(text: str):
    return embeddings.embed_query(text)


def generate_response(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content