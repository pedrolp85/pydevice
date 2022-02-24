from abc import ABCMeta, abstractmethod
from typing import List, Optional



from model.device import Device


class DevicesRepository(metaclass=ABCMeta):
    
    def __init__(self, file_source: Optional[str]):
        self._file_source = file_source

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
