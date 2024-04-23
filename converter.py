from fastapi import HTTPException
import requests
from os import getenv
import aiohttp

ALPHAVANTAGE_APIKEY=getenv('ALPHAVANTAGE_APIKEY')








async def async_converter(from_currency: str, to_currency:str, price:float):
    url=f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
    except Exception as error:
        raise HTTPException(status_code=400,detail=error)
    
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400,detail=data)
    
    exchange_rate=float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    nome_moeda=str(data["Realtime Currency Exchange Rate"]["4. To_Currency Name"])
    
    return {f"{nome_moeda} - {to_currency}": f"{price*exchange_rate:.2f}"}



