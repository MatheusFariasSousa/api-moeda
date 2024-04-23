from fastapi import APIRouter,Path,Query
from converter import async_converter
from asyncio import gather
from schema import ConverterInput,ConverterOutput


router = APIRouter()

@router.get('/converter/{from_currency}',response_model=ConverterOutput)
async def async_converter_router(body:ConverterInput,
                                from_currency:str =Path(max_length=3,regex='^[A-Z]{3}$'),
                                 ):
    to_currencies=body.to_currencies
    price=body.price
    coroutine=[]
    
    for currency in to_currencies:
        coro= async_converter(from_currency=from_currency,
        to_currency=currency,
        price=price)
        
        coroutine.append(coro)

    result= await gather(*coroutine)
    return ConverterOutput(
        message="success",
        data=result
    )
