from fastapi import APIRouter, Body, Depends, status

from store.schemas.product import ProductIn, ProductOut
from store.usecases.product import ProductUseCases

router = APIRouter(tags=["products"])

@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(body: ProductIn = Body(...), usecases: ProductUseCases = Depends()) -> ProductOut:
    return await usecases.create(body=body)