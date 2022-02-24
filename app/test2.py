from pathlib import Path
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

string_enum = "unknown"
obj = Device_State.UNKNOWN

print ("***")
print(Device_State(string_enum))
print ("***")

print(type(obj))
print(obj.value)
print(obj.__class__.__name__)



current_dir = Path(__file__)
# project_dir = [p for p in current_dir.parents if p.parts[-1]=='app'][0]
project_dir = next(p for p in current_dir.parents if p.name == "app")

# for p in current_dir.parents:
#     print(type(p))
#     print(p)

print(project_dir)


# print(build_type_dump(dictionary))
# print(build_type_dump(dictionary_nested))
