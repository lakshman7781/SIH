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
            "Experience": {
                "type": "string",
                "description": "experience of the candidate"
            },
            "Skills": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "skills of the candidate"
            },
            "Education": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "education of the candidate"
            },
            "Certifications": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "certifications of the candidate"
            },
            "Leadership_Roles": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "leadership roles of the candidate"
            },
            "Projects": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "projects of the candidate"
            },
        },
        "required": ["candidate_name","mobile_number","email_id","linkedin_profile","github_profile","Experience", "Skills", "Education", "Certifications", "Leadership_Roles", "Projects"],
    },
}