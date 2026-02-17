# main.py

from chains import job_chain, resume_chain, cover_chain
from prompts import job_parser, resume_parser

# ---- Step 1: Job Description ----
job_description = input("Enter Job Description:\n")

job_response = job_chain.invoke({
    "job_description": job_description
})

job_details = job_parser.parse(job_response.content)

print("\nExtracted Job Details:")
print(job_details)


# ---- Step 2: Resume ----
resume_text = input("\nEnter Resume Content:\n")

resume_response = resume_chain.invoke({
    "job_details": job_details,
    "resume": resume_text
})

suggestions = resume_parser.parse(resume_response.content)

print("\nResume Suggestions:")
print(suggestions)


# ---- Step 3: Cover Letter ----
cover_letter = cover_chain.invoke({
    "job_details": job_details,
    "resume": resume_text
})

print("\nGenerated Cover Letter:\n")
print(cover_letter)
