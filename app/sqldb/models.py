from sqlalchemy import Column, ForeignKey, Integer, String

from .database import Base


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True)
    model = Column(String)
    mgmt_interface_id = Column(Integer, ForeignKey("l3interfaces.id"))
    manufacturer_id = Column(Integer, ForeignKey("manufacturer.id"))


class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    enterprise_name = Column(String)


class L3Interface(Base):
    __tablename__ = "l3interface"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip_address = Column(String)
