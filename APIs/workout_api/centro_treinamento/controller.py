from typing import List
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select

from contrib.dependencias import DataBaseDependency
from workout_api.centro_treinamento.schemas import CentroTreimanetoIn, CentroTreinamentoOut
from workout_api.centro_treinamento.models import CentroTreinamentoModels

router = APIRouter()

@router.post(
        "/",
        summary="Criar um novo Centro de Treinamento",
        status_code=status.HTTP_201_CREATED,
        response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DataBaseDependency,
      centro_treinamento_in: CentroTreimanetoIn = Body(...)
) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModels(**centro_treinamento_out.model_dump())

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out

@router.get(
        "/",
        summary="Consultar todos os centros de treinamento",
        status_code=status.HTTP_200_OK,
        response_model=List(CentroTreinamentoOut),
)
async def query(id: UUID4, db_session: DataBaseDependency) -> List(CentroTreinamentoOut):
    centro_treinamento_out: List(CentroTreinamentoOut) = (await db_session.execute(select(CentroTreinamentoModels))).scalars().all()
    
    return centro_treinamento_out

@router.get(
        "/(id)",
        summary="Consultar um centro de treinamento pelo id",
        status_code=status.HTTP_200_OK,
        response_model=CentroTreinamentoOut,
)
async def query(db_session: DataBaseDependency) -> CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModels).filter_by(id=id))).scalars().all()

    if not centro_treinamento_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Centro de treinamento não encontrado pelo id: {id}"
        )

    return centro_treinamento_out
