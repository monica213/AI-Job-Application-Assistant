# chains.py

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from prompts import job_prompt, resume_prompt, cover_prompt

# Load Ollama model
llm = ChatOllama(
    model="llama3",
    temperature=0
)

# Create chains using LCEL (New Method)
job_chain = job_prompt | llm
resume_chain = resume_prompt | llm
cover_chain = cover_prompt | llm | StrOutputParser()
