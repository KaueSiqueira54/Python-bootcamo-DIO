

from typing import Annotated
from pydantic import Field

class CentroTreimaneto(BaseSchema):
    nome: Annotated(str, Field(description="Nome do centro de treinamento", example="TK-trainner", max_lenght=20))
    endereco: Annotated(str, Field(description="Endereço do centro de treinamento", example="Rua x, 002", max_lenght=60))
    proprietario: Annotated(str, Field(description="Proprietário do centro de treinamento", example="Marcos", max_lenght=30))

