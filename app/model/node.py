import ipaddress

from pydantic import BaseModel


class Node(BaseModel):
    id: int
    name: str
    ip_address: ipaddress.IPv4Address
