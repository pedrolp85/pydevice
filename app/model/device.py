from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Device_State(Enum):
    UNKNOWN = 0
    PASSIVE = 1
    ACTIVE = 2


class Device(BaseModel):
    id: int
    name: str
    manufacturer_id: int
    model: str
    state: Optional[Device_State]
    mgmt_interface_id: int
