from abc import ABCMeta, abstractmethod
from typing import List, Optional

from model.interface import L3Interface


class InterfacesRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_interface(self, id: int) -> L3Interface:
        pass

    @abstractmethod
    def create_interface(self, interface: L3Interface) -> None:
        pass

    @abstractmethod
    def update_interface(self, id: int, interface: L3Interface) -> None:
        pass

    def get_interfaces(
        self, device: Optional[str] = None, device_id: Optional[int] = None
    ) -> List[L3Interface]:
        return self._interfaces
