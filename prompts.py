# prompts.py

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from models import JobDetails, ResumeSuggestions


# -------- Feature 1 --------
job_parser = PydanticOutputParser(pydantic_object=JobDetails)

job_prompt = PromptTemplate(
    template="""
Extract structured job information.

{format_instructions}

Job Description:
{job_description}
""",
    input_variables=["job_description"],
    partial_variables={
        "format_instructions": job_parser.get_format_instructions()
    },
)


# -------- Feature 2 --------
resume_parser = PydanticOutputParser(pydantic_object=ResumeSuggestions)

resume_prompt = PromptTemplate(
    template="""
You are an AI Resume Expert.

Compare Job Details and Resume.

{format_instructions}

Job Details:
{job_details}

Resume:
{resume}
""",
    input_variables=["job_details", "resume"],
    partial_variables={
        "format_instructions": resume_parser.get_format_instructions()
    },
)


# -------- Feature 3 --------
cover_prompt = PromptTemplate(
    template="""
Write a professional cover letter.

Job Details:
{job_details}

Candidate Resume:
{resume}

Rules:
- 3 to 4 paragraphs
- Professional tone
- Plain text only
""",
    input_variables=["job_details", "resume"],
)
