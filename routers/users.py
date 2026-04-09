from fastapi import FastAPI, APIRouter, HTTPException
from helpers import save_users, load_users, normalize_phone
from schemas import User
import json

router = APIRouter(prefix="/users", tags=["Users"])



@router.get('/')
def get_all_users():
    users = load_users()
    return {"status": 200, "data": users}

@router.post('/create')
def create_user(data: User):
    users = load_users()
    new_user = data.model_dump()
    for user in users:
        if normalize_phone(user["phone"]) == normalize_phone(new_user["phone"]):
            raise HTTPException(status_code=400, detail="User already registered with the same phone number.")

    new_user_id = len(users) + 1
    new_user["id"] = f"USR-{new_user_id}"  
    users.append(new_user)    
    save_users(users)
    return {"status": 201,"data": new_user, "message": "User registered successfully"}

@router.get("/user/{user_id}")
def get_user_by_id(user_id: str):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            return {"status": 200, "data": user}
        
    raise HTTPException(status_code=404, detail="User not found with this id")