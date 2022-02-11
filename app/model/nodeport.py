from model.node import Node
from pydantic import BaseModel, validator


class NodePort(BaseModel):
    id: int
    node: Node
    port: int

    @validator("port")
    def port_range_validator(cls, v):
        if v not in range(
            1,
            65535,
        ):
            raise ValueError("Port must be an int between 1-65535")
        return v
