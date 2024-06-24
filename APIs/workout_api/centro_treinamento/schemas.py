

from typing import Annotated
from pydantic import UUID4, Field
from contrib.schemas import BaseSchema

class CentroTreimanetoIn(BaseSchema):
    nome: Annotated(str, Field(description="Nome do centro de treinamento", example="TK-trainner", max_lenght=20))
    endereco: Annotated(str, Field(description="Endereço do centro de treinamento", example="Rua x, 002", max_lenght=60))
    proprietario: Annotated(str, Field(description="Proprietário do centro de treinamento", example="Marcos", max_lenght=30))

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated(str, Field(description="Nome do centro de treinamento", example="TK-trainner", max_lenght=20))

class CentroTreinamentoOut(CentroTreimanetoIn):
    id: Annotated(UUID4, Field(description="Identificador do Centro de Treinamento"))
