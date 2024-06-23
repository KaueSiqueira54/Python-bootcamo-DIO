from fastapi import APIRouter, Body, status

from contrib.dependencias import DataBaseDependency
from workout_api.atleta.schemas import AtletaIn

router = APIRouter()

@router.post(
        "/",
        summary="Criar novo atleta",
        status_code=status.HTTP_201_CREATED 
)
async def post(
    db_session: DataBaseDependency,
      atleta_in: AtletaIn = Body(...)
):
    pass
