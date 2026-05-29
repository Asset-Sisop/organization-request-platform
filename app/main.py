from fastapi import FastAPI
from fastapi import Depends

from sqlalchemy import text

from app.database import Base
from app.database import engine

from app.models.user import User
from app.models.company import Company
from app.models.request import ClientRequest

from app.api.auth import router as auth_router
from app.api.company import router as company_router

from app.dependencies import get_current_user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(company_router)


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        return {
            "database": "connected",
            "result": result.scalar()
        }


@app.get("/me")
def read_users_me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email
    }