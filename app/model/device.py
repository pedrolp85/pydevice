from enum import Enum
from typing import List, Optional

from model.interface import L3Interface
from model.virtualserver import VirtualServer
from pydantic import BaseModel


class Device_State(Enum):
    UNKNOWN = 0
    PASSIVE = 1
    ACTIVE = 2


class Device(BaseModel):
    id: int
    name: str
    manufacturer: str
    model: str
    state: Optional[Device_State]
    mgmt_interface: Optional[L3Interface]
    interfaces: Optional[List[L3Interface]]
    virtual_servers: Optional[List[VirtualServer]]
