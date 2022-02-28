from pydantic import BaseModel


class DeviceBase(BaseModel):
    model: str
    manufacturer_id: int
    mgmt_interface_id: int


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: int

    class Config:
        orm_mode = True


class ManufacturerBase(BaseModel):
    name: str
    enterprise_name: str


class ManufacturerCreate(ManufacturerBase):
    pass


class Manufacturer(ManufacturerBase):
    id: int

    class Config:
        orm_mode = True
