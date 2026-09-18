
from pydantic import BaseModel, Field
from typing import Literal

class MenuCreate(BaseModel):
    nama: str = Field(min_length=2, max_length=100)
    sku: str = Field(pattern=r'^KOPI-\d{3}$')
    kategori: Literal['kopi','non-kopi','makanan']

class MenuOut(BaseModel):
    id: int
    nama: str
    sku: str
    kategori: str
