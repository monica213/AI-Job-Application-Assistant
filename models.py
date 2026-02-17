# models.py

from pydantic import BaseModel
from typing import List, Optional

class JobDetails(BaseModel):
    job_title: str
    required_skills: List[str]
    experience_required: Optional[int]
    tools: List[str]
    soft_skills: List[str]


class ResumeSuggestions(BaseModel):
    missing_skills: List[str]
    improvement_points: List[str]
    overall_fit_summary: str
