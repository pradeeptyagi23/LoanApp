from fastapi import FastAPI
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Sample balance sheet
sheet = [
    {
        "year": 2020,
        "month": 12,
        "profitOrLoss": 250000,
        "assetsValue": 1234
    },
    {
        "year": 2020,
        "month": 11,
        "profitOrLoss": 1150,
        "assetsValue": 5789
    },
    {
        "year": 2020,
        "month": 10,
        "profitOrLoss": 2500,
        "assetsValue": 22345
    },
    {
        "year": 2020,
        "month": 9,
        "profitOrLoss": -187000,
        "assetsValue": 223452
    }
]

#Pydantic class to check parmaters input type and validate.
class LoanApplication(BaseModel):
    business_name: str
    year_established: str
    loan_amount: float
    accounting_provider: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Business Loan Application System"}

@app.post("/application")
def create_application(application: LoanApplication):
    # initiate application
    business_name = application.business_name
    year_established = application.year_established
    loan_amount = float(application.loan_amount)
    accounting_provider = application.accounting_provider

    # fetch balance sheet from accounting provider
    balance_sheet = fetch_balance_sheet(accounting_provider)

    # apply rules to summarise application
    pre_assessment = apply_rules(balance_sheet, loan_amount)

    # send application to decision engine
    decision = send_to_decision_engine(business_name, year_established, balance_sheet, pre_assessment)

    return {"decision": decision}

def fetch_balance_sheet(accounting_provider: str) -> List[Dict[str, int]]:
    # simulate fetching balance sheet from accounting provider
    return sheet

def apply_rules(balance_sheet: List[Dict[str, int]], loan_amount: float) -> int:
    # rule 1: if profit in last 12 months preassessment set to 60
    # rule 2 : if average asset value accross 12 months > loan amount set preassessment to 100
    last_twelve_months = balance_sheet[:12]
    has_profit = any(transaction["profitOrLoss"] > 0 for transaction in last_twelve_months)
    average_asset_value = sum(transaction["assetsValue"] for transaction in last_twelve_months) / len(last_twelve_months)
    if has_profit:
        if average_asset_value < loan_amount:
            return 60
        else:
            return 100
    else:
        # default rule
        return 20

def send_to_decision_engine(business_name: str, year_established: str, balance_sheet: List[Dict[str, int]], pre_assessment: int) -> Dict[str, str]:
    # simulate sending application to decision engine
    decision = {"business_name": business_name, "year_established": year_established, "pre_assessment": pre_assessment}
    return decision