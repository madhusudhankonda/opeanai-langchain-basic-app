import os
import config

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings


OPENAI_API_KEY = config.OPENAI_API_KEY

def get_llm():
    llm = ChatOpenAI()

    return llm

def get_embeddings():
    
    openai_embeddings = OpenAIEmbeddings()

    return openai_embeddings
