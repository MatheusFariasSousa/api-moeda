from pydantic import BaseModel, Field,validator
from re import match
from typing import List

class ConverterInput(BaseModel):
    price:float = Field(gt=0)
    to_currencies:List[str]

    @validator("to_currencies")
    def validar(cls,value):
        for currency in value:
            if not match("^[A-Z]{3}$",currency):
                raise  ValueError(f"Invalid -> {currency} ")
        return value

class ConverterOutput(BaseModel):
    message:str
    data:List[dict]