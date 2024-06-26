
from pydantic import UUID4, BaseModel


class BaseSchemaMixin(BaseModel):
    class Config:
        from_atributes=True
