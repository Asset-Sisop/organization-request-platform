from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class ClientRequest(Base):
    __tablename__ = "client_requests"

    id = Column(Integer, primary_key=True, index=True)

    client_name = Column(String)

    client_phone = Column(String)

    description = Column(String)

    status = Column(String, default="new")

    company_id = Column(
        Integer,
        ForeignKey("companies.id")
    )

    company = relationship("Company")