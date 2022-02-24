from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Device_State(str, Enum):
    UNKNOWN = 'unknown'
    PASSIVE = 'passive'
    ACTIVE = 'active'


class Device(BaseModel):
    id: int
    name: str
    manufacturer_id: int
    model: str
    state: Device_State
    mgmt_interface_id: int
