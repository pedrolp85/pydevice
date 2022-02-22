import configparser
import ipaddress
import json
from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional

from model.device import Device, Device_State
from pydantic.json import pydantic_encoder
from repository.exceptions import DeviceAlreadyExistsException, DeviceNotFoundException


class DevicesRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_device(self, id: int) -> Device:
        pass

    @abstractmethod
    def create_device(self, device: Device) -> None:
        pass

    @abstractmethod
    def update_device(self, id: int, device: Device) -> None:
        pass

    def get_devices(self, manufacturer: Optional[str] = None) -> List[Device]:
        if manufacturer:
            return [
                device
                for device in self._devices
                if device.manufacturer.name == manufacturer
            ]
        else:
            return self._devices
