from uuid import UUID as PG_UID, uuid4
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

#Classe pai dos models

class BaseModel(DeclarativeBase):
    id: Mapped(PG_UID) = mapped_column(PG_UID(as_wide=True), default=uuid4, nullable=False)
