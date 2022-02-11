from typing import List

from model.device import Device
from pydantic import BaseModel


class Cluster(BaseModel):
    id: int
    cluster_name: str
    devices: List[Device]
