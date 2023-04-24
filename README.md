Business Loan Application System
This is a simple FastAPI / React based system that simulates a business loan application system. It includes an endpoint that receives an application in JSON format, retrieves a balance sheet for the business from a fake accounting provider, applies some rules to calculate a pre-assessment score, and sends the application and score to a decision engine.
The results are then render on the react frontend for viewing.


Requirements
To run this application, you need docker and docker-compose. Below are the steps to run on local machine:

1. git clone https://github.com/pradeeptyagi23/LoanApp.git
2. cd LoadApp
3. docker-compose up --build

This will install all depedencies for the frontend and backend server

To launch the frontend . Go to http://localhost:3000
The backend server will run on http://localhost:8000 and the swagger documentation will be at /docs on the backend server url


API endpoints
The service provides the following endpoints:

GET /
Returns a welcome message:
Content-Type: application/json

{
    "message": "Welcome to the Business Loan Application System"
}


POST /application
Receives an application in JSON format, fetches a balance sheet for the business, applies some rules to calculate a pre-assessment score, and sends the application and score to a decision engine. The JSON schema for the application is:

{
    "business_name": "string",
    "year_established": "string",
    "loan_amount": "string",
    "accounting_provider": "string"
}
The loan_amount field is a string that can represent a floating-point number, to avoid potential issues with the JSON serialization of large or small numbers. The service converts it to a float internally.

The response contains the decision made by the decision engine, in JSON format:

{
    "business_name": "string",
    "year_established": "string",
    "pre_assessment": 60
}
The pre_assessment field is an integer between 0 and 100.