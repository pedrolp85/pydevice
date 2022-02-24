import ipaddress

from pydantic import BaseModel


class L3Interface(BaseModel):
    id: int
    name: str
    ip_address: ipaddress.IPv4Address
    device_id: int
    ttl: int
