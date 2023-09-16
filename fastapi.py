from fastapi import APIrouter 
from jose import jwt


carlos = APIrouter

@carlos.get("direccion/")
async def direccionar():
    return "direction"
