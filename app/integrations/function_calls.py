from enum import Enum

class DocumentType(Enum):
    RESUME = "Resume"
    COVER_LETTER = "CoverLetter"
    JOB_DESCRIPTION = "JobDescription"
    MARKS_MEMO = "MarksMemo"
    AADHAAR = "Aadhaar"
    PAN = "Pan"
    JOB_APPLICATION = "JobApplication"
    LEAVE_REQUEST = "LeaveRequest"
    PERFORMANCE_REVIEW = "PerformanceReview"
    PAYROLL_DOCUMENT = "PayrollDocument"

def get_function_call(document_type: DocumentType):
    if document_type == DocumentType.RESUME:
        return func_resume_details
    elif document_type == DocumentType.MARKS_MEMO:
        return func_marks_memo
    elif document_type == DocumentType.AADHAAR:
        return func_aadhaar_details  
    elif document_type == DocumentType.PAN:
        return func_pan_details
    elif document_type == DocumentType.JOB_APPLICATION:
        return func_job_application_details
    elif document_type == DocumentType.LEAVE_REQUEST:
        return func_leave_request_details
    elif document_type == DocumentType.PAYROLL_DOCUMENT:
        return func_job_payroll_document_details
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
func_marks_memo ={
  "name": "get_academic_report_details",
  "description": "Get the academic performance details of the student from the report",
  "parameters": {
    "type": "object",
    "properties": {
      "student_name": {
        "type": "string",
        "description": "Name of the student"
      },
      "registration_number": {
        "type": "string",
        "description": "Registration number of the student"
      },
      "branch": {
        "type": "string",
        "description": "Branch of study (e.g., Computer Science and Design)"
      },
      "year_of_study": {
        "type": "string",
        "description": "Current year of study (e.g., III Year)"
      },
      "semester": {
        "type": "string",
        "description": "Current semester (e.g., II Semester)"
      },
      "courses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "course_title": {
              "type": "string",
              "description": "Title of the course"
            },
            "grade": {
              "type": "string",
              "description": "Grade received for the course"
            },
            "credits": {
              "type": "number",
              "description": "Credits for the course"
            }
          }
        },
        "description": "List of courses with grades and credits"
      },
      "SGPA": {
        "type": "number",
        "description": "Semester Grade Point Average"
      },
      "CGPA": {
        "type": "number",
        "description": "Cumulative Grade Point Average"
      },
      "date_of_issue": {
        "type": "string",
        "description": "Date of issue of the report"
      }
    },
    "required": [
      "student_name",
      "registration_number",
      "branch",
      "year_of_study",
      "semester",
      "courses",
      "SGPA",
      "CGPA",
      "date_of_issue"
    ]
  }
}
func_aadhaar_details ={
  "name": "get_aadhaar_details",
  "description": "Get the personal details of the individual from the Aadhaar card",
  "parameters": {
    "type": "object",
    "properties": {
      "aadhaar_number": {
        "type": "string",
        "description": "12-digit Aadhaar number of the individual"
      },
      "name": {
        "type": "string",
        "description": "Full name of the individual as per Aadhaar"
      },
      "date_of_birth": {
        "type": "string",
        "description": "Date of birth of the individual (in DD/MM/YYYY format)"
      },
      "gender": {
        "type": "string",
        "description": "Gender of the individual (Male/Female/Other)"
      },
      "address": {
        "type": "object",
        "properties": {
          "house_no": {
            "type": "string",
            "description": "House or apartment number"
          },
          "street": {
            "type": "string",
            "description": "Street name"
          },
          "locality": {
            "type": "string",
            "description": "Locality or area"
          },
          "city": {
            "type": "string",
            "description": "City name"
          },
          "state": {
            "type": "string",
            "description": "State name"
          },
          "pincode": {
            "type": "string",
            "description": "Postal code or ZIP code"
          }
        },
        "description": "Complete address as per Aadhaar card"
      },
      "date_of_issue": {
        "type": "string",
        "description": "Date of issue of the Aadhaar card"
      }
    },
    "required": [
      "aadhaar_number",
      "name",
      "date_of_birth",
      "gender",
      "address",
      "date_of_issue"
    ]
  }
}
func_pan_details ={
  "name": "get_pan_details",
  "description": "Get the personal details of the individual from the PAN card",
  "parameters": {
    "type": "object",
    "properties": {
      "pan_number": {
        "type": "string",
        "description": "10-character PAN number of the individual"
      },
      "name": {
        "type": "string",
        "description": "Full name of the individual as per PAN card"
      },
      "father_name": {
        "type": "string",
        "description": "Father's name of the individual as per PAN card"
      },
      "date_of_birth": {
        "type": "string",
        "description": "Date of birth of the individual (in DD/MM/YYYY format)"
      },
      "gender": {
        "type": "string",
        "description": "Gender of the individual (Male/Female/Other)(optional)"
      },
      "date_of_issue": {
        "type": "string",
        "description": "Date of issue of the PAN card"
      }
    },
    "required": [
      "pan_number",
      "name",
      "father_name",
      "date_of_birth",
      "gender",
      "date_of_issue"
    ]
  }
}
func_job_application_details ={
  "name": "job_application_details",
  "description": "Collect the details of the individual applying for a job",
  "parameters": {
    "type": "object",
    "properties": {
      "full_name": {
        "type": "string",
        "description": "Full name of the applicant"
      },
      "email": {
        "type": "string",
        "description": "Email address of the applicant"
      },
      "phone_number": {
        "type": "string",
        "description": "Contact number of the applicant"
      },
      "date_of_birth": {
        "type": "string",
        "description": "Date of birth of the applicant (in DD/MM/YYYY format)"
      },
      "gender": {
        "type": "string",
        "description": "Gender of the applicant (Male/Female/Other)(optional)"
      },
      "position_applied_for": {
        "type": "string",
        "description": "Job position that the applicant is applying for"
      },
      "experience_years": {
        "type": "number",
        "description": "Number of years of work experience"
      },
      "skills": {
        "type": "array",
        "description": "List of skills possessed by the applicant",
        "items": {
          "type": "string"
        }
      },
      "education": {
        "type": "string",
        "description": "Highest level of education completed by the applicant"
      },
      "resume_link": {
        "type": "string",
        "description": "Link to the applicant's resume"
      }
    },
    "required": [
      "full_name",
      "email",
      "phone_number",
      "date_of_birth",
      "position_applied_for",
      "experience_years",
      "skills",
      "education",
      "resume_link"
    ]
  }
}
func_leave_request_details ={
  "name": "leave_request_details",
  "description": "Collect the details of the individual requesting leave",
  "parameters": {
    "type": "object",
    "properties": {
      "employee_id": {
        "type": "string",
        "description": "Unique identifier for the employee"
      },
      "full_name": {
        "type": "string",
        "description": "Full name of the employee"
      },
      "email": {
        "type": "string",
        "description": "Email address of the employee"
      },
      "department": {
        "type": "string",
        "description": "Department in which the employee works"
      },
      "leave_type": {
        "type": "string",
        "description": "Type of leave (e.g., Annual, Sick, Maternity, etc.)"
      },
      "start_date": {
        "type": "string",
        "description": "Start date of the leave (in DD/MM/YYYY format)"
      },
      "end_date": {
        "type": "string",
        "description": "End date of the leave (in DD/MM/YYYY format)"
      },
      "reason_for_leave": {
        "type": "string",
        "description": "Reason for requesting leave"
      },
      "contact_during_leave": {
        "type": "string",
        "description": "Contact information during the leave period (optional)"
      },
      "approver_id": {
        "type": "string",
        "description": "ID of the manager or approver for the leave"
      }
    },
    "required": [
      "employee_id",
      "full_name",
      "email",
      "department",
      "leave_type",
      "start_date",
      "end_date",
      "reason_for_leave",
      "approver_id"
    ]
  }
}
func_job_payroll_document_details ={
  "name": "payroll_document_details",
  "description": "Collect the details of the employee's payroll document",
  "parameters": {
    "type": "object",
    "properties": {
      "employee_id": {
        "type": "string",
        "description": "Unique identifier for the employee"
      },
      "full_name": {
        "type": "string",
        "description": "Full name of the employee"
      },
      "email": {
        "type": "string",
        "description": "Email address of the employee"
      },
      "department": {
        "type": "string",
        "description": "Department in which the employee works"
      },
      "pay_period_start": {
        "type": "string",
        "description": "Start date of the payroll period (in DD/MM/YYYY format)"
      },
      "pay_period_end": {
        "type": "string",
        "description": "End date of the payroll period (in DD/MM/YYYY format)"
      },
      "basic_salary": {
        "type": "number",
        "description": "Basic salary of the employee for the pay period"
      },
      "bonuses": {
        "type": "number",
        "description": "Total bonuses earned during the pay period (optional)"
      },
      "deductions": {
        "type": "number",
        "description": "Total deductions for the pay period (e.g., taxes, insurance)"
      },
      "net_salary": {
        "type": "number",
        "description": "Net salary after all deductions"
      },
      "payment_date": {
        "type": "string",
        "description": "Date when the salary was paid (in DD/MM/YYYY format)"
      },
      "payment_method": {
        "type": "string",
        "description": "Method of payment (e.g., Bank Transfer, Cheque)"
      },
      "bank_account_details": {
        "type": "string",
        "description": "Bank account details where the salary was deposited (optional)"
      }
    },
    "required": [
      "employee_id",
      "full_name",
      "email",
      "department",
      "pay_period_start",
      "pay_period_end",
      "basic_salary",
      "deductions",
      "net_salary",
      "payment_date",
      "payment_method"
    ]
  }
}




