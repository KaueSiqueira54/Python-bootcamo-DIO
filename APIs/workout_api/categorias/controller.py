from fastapi import APIRouter, Body, status

from contrib.dependencias import DataBaseDependency
from workout_api.categorias.schemas import Categoria

router = APIRouter()

@router.post(
        "/",
        summary="Criar uma nova categoria",
        status_code=status.HTTP_201_CREATED 
)
async def post(
    db_session: DataBaseDependency,
      atleta_in: Categoria = Body(...)
):
    pass