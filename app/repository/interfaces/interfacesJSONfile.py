import json
from pathlib import Path
from typing import List

from model.interface import L3Interface
from pydantic.json import pydantic_encoder
from repository.exceptions import (
    InterfaceAlreadyExistsException,
    InterfaceNotFoundException,
)

from .interfaces import InterfacesRepository


class InterfacesRepositoryJSONFile(InterfacesRepository):
    def __init__(self, file_name: str = "interfaces.json") -> None:
        self._file_name = file_name
        self._interfaces = (
            self._get_interfaces_from_json_file() if Path(file_name).is_file() else []
        )

    def _get_interfaces_from_json_file(self) -> List[L3Interface]:
        with open(self._file_name, mode="r") as f:
            raw_interfaces = f.read()
            interfaces = json.loads(raw_interfaces)
            return [L3Interface(**p) for p in interfaces]
        return []

    def _save_interfaces_to_json_file(self) -> None:
        interfaces_to_save = [p.dict() for p in self._interfaces]
        with open(self._file_name, mode="w") as f:
            data = json.dumps(interfaces_to_save, indent=4, default=pydantic_encoder)
            f.write(data)

    def get_interface(self, id: int) -> L3Interface:
        self._get_interfaces_from_json_file()
        for interface in self._interfaces:
            if interface.id == id:
                return interface
        raise InterfaceNotFoundException(id)

    def create_interface(self, interface: L3Interface) -> None:
        try:
            self.get_interface(interface.id)
        except InterfaceNotFoundException:
            self._interfaces.append(device)
            self._save_interfaces_to_json_file()
        else:
            raise InterfaceAlreadyExistsException(device.id)

    def update_interface(self, id: int, interface: L3Interface) -> None:
        if not self.get_interface(id):
            raise InterfaceNotFoundException(id)
        else:
            pass
