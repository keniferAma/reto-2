from pydantic import BaseModel, PrivateAttr


class Ateo(BaseModel):
    name: str
    surname: str
    _age: int = PrivateAttr(default=32)


