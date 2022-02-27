import json
from pathlib import Path
from typing import List, Optional, Any

from model.interface import L3Interface
from pydantic.json import pydantic_encoder
from repository.exceptions import (
    InterfaceAlreadyExistsException,
    InterfaceNotFoundException,
)
from settings import *

from .interfaces import InterfacesRepository


class InterfacesRepositoryJSONFile(InterfacesRepository):
    def __init__(self, file_source: Optional[str] ) -> None:
        super().__init__(file_source)        
        self._file_name = self._get_dir(self._file_source)
        self._interfaces = (
            self._get_interfaces_from_json_file()
            if Path(self._file_name).is_file()
            else []
        )

    def _get_dir(self, file_name: str) -> Path:
        return Path(__file__).parent.parent.parent / self._file_source / "interfaces.json"

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

    def create_interface(self, interface: L3Interface) -> Any:
        try:
            self.get_interface(interface.id)
        except InterfaceNotFoundException:
            self._interfaces.append(interface)
            self._save_interfaces_to_json_file()
            return interface
        else:
            raise InterfaceAlreadyExistsException(device.id)

    def update_interface(self, id: int, interface: L3Interface) -> None:
        if not self.get_interface(id):
            raise InterfaceNotFoundException(id)
        else:
            pass
