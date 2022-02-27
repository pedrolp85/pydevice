import configparser
from pathlib import Path
from typing import List, Optional

from model.interface import L3Interface
from repository.exceptions import (
    InterfaceAlreadyExistsException,
    InterfaceNotFoundException,
)
from settings import *

from .interfaces import InterfacesRepository


class InterfacesRepositoryINIFile(InterfacesRepository):
    def __init__(self, file_source: Optional[str] ) -> None:
        super().__init__(file_source)        
        self._file_name = self._get_dir(self._file_source)
        self._interfaces = (
            self._get_interfaces_from_ini_file()
            if Path(self._file_name).is_file()
            else []
        )

    def _get_dir(self, file_name: str) -> Path:
        return Path(__file__).parent.parent.parent / self._file_source / "interfaces.ini"

    def _get_interfaces_from_ini_file(self) -> List[L3Interface]:
        ini_parser = configparser.ConfigParser()
        ini_parser.read(self._file_name)
        interface_list = []
        for section in ini_parser.sections():
            interface_dictionary = {
                option: ini_parser.get(section, option)
                for option in ini_parser.options(section)
            }
            interface_dictionary.update({"name": section})
            interface_list.append(L3Interface(**interface_dictionary))

        return interface_list

    def _save_interfaces_to_ini_file(self) -> None:
        interfaces_to_save = [p.dict() for p in self._interfaces]
        parser = configparser.ConfigParser()
        for interface in interfaces_to_save:
            parser.add_section(interface["name"])
            for k, v in interface.items():
                if v and k != "name":
                    parser.set(interface["name"], k, str(v))
        with open(self._file_name, "w") as configfile:
            parser.write(configfile)

    def get_interface(self, id: int) -> L3Interface:
        self._get_interfaces_from_ini_file()
        for interface in self._interfaces:
            if interface.id == id:
                return interface
        raise InterfaceNotFoundException(id)

    def create_interface(self, interface: L3Interface) -> None:
        try:
            self.get_interface(interface.id)
        except InterfaceNotFoundException:
            self._interfaces.append(interface)
            self._save_interfaces_to_ini_file()
            return interface
        else:
            raise InterfaceAlreadyExistsException(device.id)

    def update_interface(self, id: int, interface: L3Interface) -> None:
        try:
            self.get_interface(interface.id)
        except InterfaceNotFoundException:
            pass
        else:
            raise InterfaceAlreadyExistsException(interface.id)
