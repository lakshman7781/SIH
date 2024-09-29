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
    TIMETABLE = "TimeTable"
    PANCARD = "PanCard"
    OFFER_LETTER = "OfferLetter"
    EMPLOYEE_CONTRACTS = "EmployeeContracts"
    LEAVE_REQUESTS = "LeaveRequests"
    PAYROLL_DOCUMENT = "PayrollDocument"

def get_function_call(document_type: DocumentType):
    if document_type == DocumentType.RESUME:
        return func_resume_details
    elif document_type == DocumentType.COVER_LETTER:
        return func_cover_letter_details
    elif document_type == DocumentType.MARKS_MEMO:
        return func_marks_memo
    elif document_type == DocumentType.AADHAAR:
        return func_aadhaar_details
    elif document_type == DocumentType.TIMETABLE:
        return func_timetable
    elif document_type == DocumentType.PANCARD:
        return func_pancard
    elif document_type == DocumentType.OFFER_LETTER:
        return func_offer_letter
    elif document_type == DocumentType.EMPLOYEE_CONTRACTS:
        return func_employee_contracts 
    elif document_type == DocumentType.JOB_APPLICATION:
        return func_job_application_details
    elif document_type == DocumentType.PAYROLL_DOCUMENT:
        return func_job_payroll_document_details 
    else:
        raise None
        
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

func_cover_letter_details ={
  "name": "get_cover_letter_details",
  "description": "Get the details of the candidate's cover letter",
  "parameters": {
    "type": "object",
    "properties": {
      "candidate_name": {
        "type": "string",
        "description": "Name of the candidate"
      },
      "position_applied": {
        "type": "string",
        "description": "Position the candidate is applying for"
      },
      "company_name": {
        "type": "string",
        "description": "Name of the company the candidate is applying to"
      },
      "introductory_paragraph": {
        "type": "string",
        "description": "Introduction of the candidate and the purpose of the cover letter"
      },
      "professional_experience": {
        "type": "string",
        "description": "Professional experience relevant to the applied position"
      },
      "skills_highlight": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Key skills that align with the job position"
      },
      "education_mention": {
        "type": "string",
        "description": "Relevant education details briefly mentioned"
      },
      "why_this_company": {
        "type": "string",
        "description": "Reason why the candidate wants to work for this company"
      },
      "closing_paragraph": {
        "type": "string",
        "description": "Conclusion with a call to action and gratitude"
      },
      "contact_information": {
        "type": "object",
        "properties": {
          "mobile_number": {
            "type": "number",
            "description": "Mobile number of the candidate (optional) provide if available"
          },
          "email_id": {
            "type": "string",
            "description": "Email ID of the candidate (optional) provide if available"
          },
          "linkedin_profile": {
            "type": "string",
            "description": "LinkedIn profile of the candidate (optional) provide if available"
          }
        }
      }
    },
    "required": [
      "candidate_name",
      "position_applied",
      "company_name",
      "introductory_paragraph",
      "professional_experience",
      "skills_highlight",
      "closing_paragraph",
      "contact_information"
    ]
  }
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


func_timetable ={
  "name": "get_college_timetable_details",
  "description": "Get the details of the college timetable",
  "parameters": {
    "type": "object",
    "properties": {
      "timetable_id": {
        "type": "string",
        "description": "Unique ID for the timetable"
      },
      "college_name": {
        "type": "string",
        "description": "Name of the college"
      },
      "department": {
        "type": "string",
        "description": "Department for which the timetable is provided"
      },
      "year_of_study": {
        "type": "string",
        "description": "Year of study (e.g., First Year, Second Year)"
      },
      "semester": {
        "type": "string",
        "description": "Current semester (e.g., Semester 1, Semester 2)"
      },
      "class_name": {
        "type": "string",
        "description": "Class name (e.g., B.Tech Computer Science)"
      },
      "start_date": {
        "type": "string",
        "description": "Start date of the timetable (in DD/MM/YYYY format)"
      },
      "end_date": {
        "type": "string",
        "description": "End date of the timetable (in DD/MM/YYYY format)"
      },
      "schedule": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "day": {
              "type": "string",
              "description": "Day of the week (e.g., Monday, Tuesday)"
            },
            "sessions": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "subject": {
                    "type": "string",
                    "description": "Subject being taught in that session"
                  },
                  "start_time": {
                    "type": "string",
                    "description": "Start time of the session (in HH:MM format)"
                  },
                  "end_time": {
                    "type": "string",
                    "description": "End time of the session (in HH:MM format)"
                  },
                  "room_number": {
                    "type": "string",
                    "description": "Room or lab number"
                  },
                  "faculty_name": {
                    "type": "string",
                    "description": "Name of the faculty teaching the session"
                  }
                }
              },
              "description": "Sessions for a particular day"
            }
          }
        },
        "description": "Weekly schedule with subjects and session timings"
      }
    },
    "required": [
      "timetable_id",
      "college_name",
      "department",
      "year_of_study",
      "semester",
      "class_name",
      "start_date",
      "end_date",
      "schedule"
    ]
  }
}
func_pancard ={
  "name": "get_pan_card_details",
  "description": "Get the details of the individual's PAN card",
  "parameters": {
    "type": "object",
    "properties": {
      "pan_number": {
        "type": "string",
        "description": "The 10-character alphanumeric PAN number"
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
      },
      "issue_date": {
        "type": "string",
        "description": "Date of issue of the PAN card (in DD/MM/YYYY format)"
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
        "description": "Address associated with the PAN card"
      }
    },
    "required": [
      "pan_number",
      "name",
      "father_name",
      "date_of_birth",
      "gender",
      "issue_date",
      "address"
    ]
  }
}
func_offer_letter ={
  "name": "get_offer_letter_details",
  "description": "Get the details from the offer letter of the individual",
  "parameters": {
    "type": "object",
    "properties": {
      "offer_id": {
        "type": "string",
        "description": "Unique offer ID for the offer letter"
      },
      "candidate_name": {
        "type": "string",
        "description": "Name of the candidate receiving the offer"
      },
      "position": {
        "type": "string",
        "description": "Position offered to the candidate"
      },
      "company_name": {
        "type": "string",
        "description": "Name of the company offering the position"
      },
      "job_location": {
        "type": "string",
        "description": "Location where the job will be based"
      },
      "salary_package": {
        "type": "string",
        "description": "Details of the salary package offered"
      },
      "joining_date": {
        "type": "string",
        "description": "Date when the candidate is expected to join (in DD/MM/YYYY format)"
      },
      "working_hours": {
        "type": "string",
        "description": "Working hours or schedule"
      },
      "benefits": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of benefits offered (e.g., health insurance, bonuses)"
      },
      "reporting_manager": {
        "type": "string",
        "description": "Name of the candidate’s reporting manager"
      },
      "contract_terms": {
        "type": "string",
        "description": "Key terms of the contract (e.g., probation period, notice period)"
      },
      "date_of_issue": {
        "type": "string",
        "description": "Date when the offer letter was issued (in DD/MM/YYYY format)"
      }
    },
    "required": [
      "offer_id",
      "candidate_name",
      "position",
      "company_name",
      "job_location",
      "salary_package",
      "joining_date",
      "working_hours",
      "benefits",
      "reporting_manager",
      "contract_terms",
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

func_employee_contracts ={
  "name": "get_employee_contract_details",
  "description": "Get the details of an employee's contract",
  "parameters": {
    "type": "object",
    "properties": {
      "contract_id": {
        "type": "string",
        "description": "Unique identifier for the employee contract"
      },
      "employee_name": {
        "type": "string",
        "description": "Full name of the employee"
      },
      "employee_id": {
        "type": "string",
        "description": "Employee's unique identification number"
      },
      "position": {
        "type": "string",
        "description": "Position or job title of the employee"
      },
      "department": {
        "type": "string",
        "description": "Department the employee works in"
      },
      "contract_start_date": {
        "type": "string",
        "description": "The start date of the contract (in DD/MM/YYYY format)"
      },
      "contract_end_date": {
        "type": "string",
        "description": "The end date of the contract (if applicable) in DD/MM/YYYY format"
      },
      "contract_type": {
        "type": "string",
        "description": "Type of contract (e.g., Full-time, Part-time, Temporary, Permanent)"
      },
      "salary": {
        "type": "string",
        "description": "Details of the salary offered in the contract"
      },
      "benefits": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of benefits provided (e.g., health insurance, retirement plans)"
      },
      "working_hours": {
        "type": "string",
        "description": "The agreed working hours or schedule"
      },
      "notice_period": {
        "type": "string",
        "description": "Notice period for contract termination (e.g., 30 days)"
      },
      "probation_period": {
        "type": "string",
        "description": "Length of the probation period (e.g., 6 months)"
      },
      "contract_terms": {
        "type": "string",
        "description": "Key terms and conditions of the contract"
      },
      "date_of_signing": {
        "type": "string",
        "description": "The date when the contract was signed (in DD/MM/YYYY format)"
      },
      "reporting_manager": {
        "type": "string",
        "description": "Name of the reporting manager or supervisor"
      }
    },
    "required": [
      "contract_id",
      "employee_name",
      "employee_id",
      "position",
      "department",
      "contract_start_date",
      "contract_type",
      "salary",
      "working_hours",
      "notice_period",
      "contract_terms",
      "date_of_signing",
      "reporting_manager"
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
      "resume_link"    ]
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
