from typing import Annotated
from pydantic import Field, PositiveFloat

from contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated(str, Field(description="Nome do ateta", example="João", max_lenght=50))
    cpf: Annotated(str, Field(description="CPF do atleta", example="12345678900", max_lenght=11))
    idade: Annotated(int, Field(description="Idade do Atleta", example="25"))
    peso: Annotated(PositiveFloat, Field(description="Peso do Atleta", example=78.5))
    altura: Annotated(PositiveFloat, Field(description="Altura do Atleta", example=1.70))
    sexo: Annotated(PositiveFloat, Field(description="Sexo do Atleta", example="M", max_lenght=1))

class AtletaIn(Atleta):
    pass
class AtletaOut(Atleta, OutMixin):
    pass
    



