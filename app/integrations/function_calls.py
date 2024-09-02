from enum import Enum

class DocumentType(Enum):
    RESUME = "Resume"
    COVER_LETTER = "CoverLetter"
    JOB_DESCRIPTION = "JobDescription"

def get_function_call(document_type: DocumentType):
    if document_type == DocumentType.RESUME:
        return func_resume_details
    else:
        return None
       
func_resume_details = {
    "name": "get_resume_details",
    "description": "Get the details of the candidate in the resume",
    "parameters": {
        "type": "object",
        "properties": {
            "candidate_name": {
                "type": "string",
                "description": "name"
            },
            "mobile_number": {
                "type": "number",
                "description": "mobile number of the candidate (optional) provide if available"
            },
            "email_id": {
                "type": "string",
                "description": "email id of the candidate (optional) provide if available"
            },
            "linkedin_profile": {
                "type": "string",
                "description": "linkedin profile of the candidate (optional) provide if available"
            },
            "github_profile": {
                "type": "string",
                "description": "github profile of the candidate (optional) provide if available"
            },
            "experience": {
                "type": "string",
                "description": "experience of the candidate"
            },
            "skills": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "skills of the candidate"
            },
            "education": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "education of the candidate"
            },
            "certifications": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "certifications of the candidate"
            },
            "leadership_roles": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "leadership roles of the candidate"
            },
            "projects": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "projects of the candidate"
            },
        },
        "required": ["candidate_name", "mobile_number", "email_id", "linkedin_profile", "github_profile", "experience", "skills", "education", "certifications", "leadership_roles", "projects"],
    },
}