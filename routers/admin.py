from fastapi import HTTPException, APIRouter
from schemas import UpdateLoan

from helpers import load_loans, save_loans

admin = APIRouter(prefix="/admin", tags=["Admin"])

@admin.put("/update/loan/{loan_id}")
def loan_manage(loan_id: str,data: UpdateLoan):
    loans = load_loans();
    update_loan = data.model_dump()
    for loan in loans:
        if loan["id"] == loan_id:
            loan["status"] = update_loan["status"]
            loan["comment"] = update_loan["comment"]
            save_loans(loans)
            return {"status": 200, "data": loan}
        
    raise HTTPException(status_code=404, detail=f"Loan not found with {loan_id}")

    