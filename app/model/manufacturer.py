from pydantic import BaseModel


class Manufacturer(BaseModel):
    id: int
    name: str
    full_name: str
