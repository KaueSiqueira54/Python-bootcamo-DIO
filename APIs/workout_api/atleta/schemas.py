from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from contrib.schemas import BaseSchema, OutMixin
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

class Atleta(BaseSchema):
    nome: Annotated(str, Field(description="Nome do ateta", example="João", max_lenght=50))
    cpf: Annotated(str, Field(description="CPF do atleta", example="12345678900", max_lenght=11))
    idade: Annotated(int, Field(description="Idade do Atleta", example="25"))
    peso: Annotated(PositiveFloat, Field(description="Peso do Atleta", example=78.5))
    altura: Annotated(PositiveFloat, Field(description="Altura do Atleta", example=1.70))
    sexo: Annotated(PositiveFloat, Field(description="Sexo do Atleta", example="M", max_lenght=1))
    categoria: Annotated(CategoriaIn, Field(description="Categoria do atleta"))
    centro_treinamento: Annotated(CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta"))

class AtletaIn(Atleta):
    pass
class AtletaOut(Atleta, OutMixin):
    pass
    

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="Nome do ateta", example="João", max_lenght=50)]
    idade: Annotated[Optional[int], Field(None, description="Idade do Atleta", example="25")]


