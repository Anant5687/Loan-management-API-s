from fastapi import APIRouter, HTTPException
from helpers import load_loans, load_users, save_loans
from schemas import Loans
from datetime import datetime

loans = APIRouter(prefix="/loans", tags=["Loans"])

@loans.get("/")
def get_all_loans(): 
    loans = load_loans()
    return {"status": 200, "data": loans}

@loans.get("/${loan_id}/${user_id}")
def get_loan_by_id(loan_id: str, user_id: str):
    loans = load_loans()
    for loan in loans:
        if loan["id"] == loan_id and loan["user_id"] == user_id:
            return {"status": 200, "data": loan}
        elif loan["id"] == loan_id and loan["user_id"] != user_id:
            return {"status": 400, "message": "Loan does not belong to this user"}
        
    raise HTTPException(status_code=404, detail=f"loan not found with loan id: {loan_id} and user id: {user_id}")

@loans.post("/create")
def create_loan(data: Loans):
    new_loan = data.model_dump()
    users = load_users()
    loans = load_loans()

    for loan in loans:
        if loan["user_id"] == new_loan["user_id"]:
            raise HTTPException(status_code=400, detail="A loan already exist with this user id")

    user_found = False

    for user in users:
        if new_loan["user_id"] == user["id"]:
            user_found= True
            if new_loan["required_amt"] > user["yearly_income"]:
                raise HTTPException(status_code=400, detail="User income is not sufficient")

    if not user_found:
        raise HTTPException(status_code=404, detail=F"User not found with this {new_loan["user_id"]}")
    
    new_loan["id"] = f"LN-{len(loans) + 1}"
    loans.append(new_loan)
    save_loans(loans)
    return {"status": 201, "message": "Loan created successfully", "data": new_loan}