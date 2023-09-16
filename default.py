from pydantic import BaseModel, PrivateAttr


class Ateo(BaseModel):
    name: str
    surname: str
    _age: int = PrivateAttr(default=32)


persona1 = Ateo(name="alberto", surname="bedoya")

print(persona1._age)