#**HNG12 Stage 0 Task - Public API**


This is a simple backend API developed for the HNG12 Stage 0 Task. The API returns the following details in JSON format:


---Registered email address (The email i used to register on the HNG12 Slack workspace).


---The current date and time in ISO 8601 format (UTC) formatted timestamp.


---The GitHub repository URL of this project's codebase.


**Technology Stack**


--Programming Language: Python


--Framework: FastAPI


**API Specification**


**Endpoint**


**Method**: GET


**URL**: https://hng12-stage0-public-api.onrender.com/stage_zero


**Response Format**: JSON

{

  "email": "oguntayohabeebullah@gmail.com",

  "current_datetime": "2025-01-30T09:30:00Z",

  "github_url": "https://github.com/Oguntayo/hng12-stage0-public-api"

}



**Setup Instructions


Prerequisites**


--Ensure you have Python installed (version 3.7+ ).


**Installation**


---Clone the repository: "git clone https://github.com/Oguntayo/hng12-stage0-public-api.git
cd hng12-stage0-public-api"

---Create a virtual environment:"python -m venv stagezero-env"

---Activate the virtual environment:stagezero-env\Scripts\activate
Mac/Linux:source stagezero-env/bin/activate

---Install dependencies:pip install -r requirements.txt

---Run the application:uvicorn main:app --reload

The endpoint should be accessible at (http://127.0.0.1:8000/stage_zero)
Deployment


The API is deployed and publicly accessible at:
https://hng12-stage0-public-api.onrender.com/stage_zero


CORS Handling


The API is configured to handle Cross-Origin Resource Sharing (CORS) properly using FastAPI's built-in support.


**Useful Links**


Python Developers: https://hng.tech/hire/python-developers

Node.js Developers: https://hng.tech/hire/nodejs-developers

Java Developers: https://hng.tech/hire/java-developers

PHP Developers: https://hng.tech/hire/php-developers

Golang Developers: https://hng.tech/hire/golang-developers

C# Developers: https://hng.tech/hire/csharp-developers

Author
**
**Oguntayo**

GitHub: Oguntayo
