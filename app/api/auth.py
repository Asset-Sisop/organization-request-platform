from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from app.database import SessionLocal

from app.models.user import User

from app.schemas.user import UserCreate
from app.schemas.user import UserLogin

from app.security import create_access_token

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    hashed_password = pwd_context.hash(user.password)

    db_user = User(
        email=user.email,
        password_hash=hashed_password
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return {
        "message": "user created",
        "user_id": db_user.id,
        "email": db_user.email
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials"
        )

    valid_password = pwd_context.verify(
        form_data.password,
        db_user.password_hash
    )

    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }