import ipaddress
from enum import Enum

from model.pool import Pool
from pydantic import BaseModel


class Protocol(Enum):
    TCP = 1
    UDP = 2


class VirtualServer(BaseModel):
    id: int
    destination_ip_address: ipaddress.IPv4Address
    port: int
    protocol: Protocol
    pool: Pool
