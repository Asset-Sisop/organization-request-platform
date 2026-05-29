from typing import List

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.dependencies import get_current_user

from app.models.user import User
from app.models.company import Company

from app.schemas.company import CompanyCreate
from app.schemas.company import CompanyResponse

router = APIRouter(
    prefix="/companies",
    tags=["companies"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=CompanyResponse
)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_company = Company(
        name=company.name,
        description=company.description,
        owner_id=current_user.id
    )

    db.add(db_company)

    db.commit()

    db.refresh(db_company)

    return db_company


@router.get(
    "/",
    response_model=List[CompanyResponse]
)
def get_my_companies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    companies = db.query(Company).filter(
        Company.owner_id == current_user.id
    ).all()

    return companies