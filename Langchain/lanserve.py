from fastapi import FastAPI
import os
from langserve import add_routes
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleChain
from langchain.parsers import StrOutputParser
from langchain.models import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser = StrOutputParser()

# Create chain
chain = SimpleChain(prompt_template, model, parser)

# App definition
app = FastAPI(title="Langchain Server",
              version="1.0",
              description="A simple API server using Langchain runnable interfaces")
