from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, PrivateAttr


class Persona(BaseModel):
    nombre: str
    apellido: str


class Contraseña(Persona):
    _contraseña: int = PrivateAttr(default=123)