from fastapi import FastAPI
from schemas import User

from routers.users import router
from routers.loans import loans

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": 200}

app.include_router(router)
app.include_router(loans)