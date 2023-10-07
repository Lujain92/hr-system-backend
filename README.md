# HR System API
### Author : Lujain Al-Jarrah
### Version :1.0.0

the HR System API provides functionalities for managing job candidates, allowing them to register and upload their resumes. HR managers can view the list of candidates and download their resumes. Built with Django and Django REST Framework, this system ensures efficient handling of HR-related tasks.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [File Storage](#file-storage)
- [Testing](#testing)
- [Authentication](#authentication)

## Requirements

- **Python 3.x**
- **Django**: A high-level Python web framework.
- **Django REST Framework**: A powerful toolkit for building Web APIs.

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:Lujain92/hr_system_backend.git
   cd hr_system_backend
   ```

2. **Set up virtual environment:**
 *  Ubunto user :
      ```
      python -m venv .venv
      source .venv/bin/activate
      ```
* Windows  user :
   ```
   Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
   python -m venv .venv
   .venv\Scripts\activate 
   ```


3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Creating a Superuser:**

* To access the Django admin panel and manage the HR System, you can create a superuser using the following command:

    ```bash
    python manage.py createsuperuser
    ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

### Register Candidate

- **URL:** `/candidates/register/`
- **Method:** POST
- **Parameters:**
  - `full_name` (string): Candidate's full name.
  - `date_of_birth` (string): Candidate's date of birth (YYYY-MM-DD).
  - `years_of_experience` (integer): Candidate's years of experience.
  - `department` (string): Candidate's department (IT, HR, Finance).
  - `resume` (file): Candidate's resume (PDF or DOCX).
- **Response:** Candidate details if successfully registered.

### List Candidates

- **URL:** `/candidates/list/`
- **Method:** GET
- **Headers:** `X-ADMIN: 1` (Admin access only)
- **Response:** List of candidates ordered by registration date.

### Download Resume

- **URL:** `/candidates/download/<candidate_id>/`
- **Method:** GET
- **Headers:** `X-ADMIN: 1` (Admin access only)
- **Response:** Candidate's resume file (PDF or DOCX).

## File Storage

Candidate resumes are stored on the local file system.

## Testing

To run the tests, use the following command:

```bash
python manage.py test
```

## Authentication

Admin access is required for listing candidates and downloading resumes. Set the `X-ADMIN: 1` header in the request for admin access.

