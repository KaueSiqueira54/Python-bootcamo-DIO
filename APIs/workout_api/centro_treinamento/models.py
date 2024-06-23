
from contrib.models import BaseModel, Mapped, mapped_column, relationship
from contrib.models import BaseModel


class CentroTreimanetoModels(BaseModel):
    __tablename__= "centro_treinamento"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped["AtletaModel"] = relationship(back_populates="centro_treinamento")