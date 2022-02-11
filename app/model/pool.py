from typing import List

from model.nodeport import NodePort
from pydantic import BaseModel


class Pool(BaseModel):
    id: int
    nodeports: List[NodePort]
